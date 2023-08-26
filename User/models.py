from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.
class User(AbstractUser):
    class Role(models.TextChoices):                     # For setting up Role types
        ADMIN = "ADMIN", "Admin"
        STUDENT = "STUDENT", "Student"
        TEACHER = "TEACHER", "Teacher"

    base_role = Role.ADMIN     # When ever we create a superuser, it will automatically become the Admin

    role = models.CharField(max_length=50, choices=Role.choices)   # Create column named role

    def save(self, *args, **kwargs):  # For saving User info to the Database
        if not self.pk:
            self.role = self.base_role
            return super().save(*args, **kwargs)


# Student Section --------------

class StudentManager(BaseUserManager):  # Section to manage User when the Role is Student
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.STUDENT)   # Here we have to define the User Role


class Student(User):
    base_role = User.Role.STUDENT
    student = StudentManager()  # Here we declare The User is a Student

    class Meta:
        proxy = True


@receiver(post_save, sender=Student)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'STUDENT':
        StudentProfile.objects.create(user=instance)


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user


class TeacherManager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)


class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()

    class Meta:
        proxy = True


@receiver(post_save, sender=Teacher)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'TEACHER':
        TeacherProfile.objects.create(user=instance)


class TeacherProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user

