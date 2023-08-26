> ## Step 4:
> We have created a User and SuperUser on Previous Step, But we miss the way to register our Custom User table to the Admin Page.
> 
> Go to `User/admin.py` and copy and paste the following Command
```commandline
from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .models import *


# Register your models here.

class TuitionUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    # fieldsets = (
    #     (None, {'fields': ('email', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name')}),
    #     (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
    #                                    'groups', 'user_permissions')}),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    # )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'email', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), TuitionUserAdmin)
```
>
> That's all you have to do to display Custom User Table to the Admin Section
> 
> Now we have to Define and Declare a User where the role is `STUDENT`
> 
> Now copy & paste the following commend
```commandline
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

```
>
> Now again open shell and add `Stuent`. Let's see if its workout or not
> 
> As we discuss the command for shell is 
```commandline
python manage.py shell
```
>
> Code for adding `Students` in shell is same as adding `Admin` with some minor changes. 
> Following Code is used to add User as `Student`
> 
```commandline
>>> from User.models import Student
>>> Student.objects.create_user(username='AVI', email='avi@gmail.com', password='avi1234')
<Student: AVI>
```
> 
> Now How can you Check the User with role as Student
> 
```commandline
>>> Student.student.all()
<QuerySet [<Student: AVI>]>
>>>
```
>
> This is how it looks like
> ![StudentShell](../Screen%20Shots/ss11.PNG)
>
> Code to check all User is
> 
```commandline
>>> from User.models import User
>>> User.objects.all()
<QuerySet [<User: Apparky>, <User: ShadowKing>, <User: AVI>]>
>>>
```
> These are the code to check `Student` and `Admin` separately 
> 
```commandline
>>>
>>> User.objects.filter(role='STUDENT')
<QuerySet [<User: AVI>]>
>>>
>>>
>>> User.objects.filter(role='ADMIN')
<QuerySet [<User: Apparky>, <User: ShadowKing>]>
>>>
```
>
> This is how it looks like
> 
> ![UserShell](../Screen%20Shots/ss12.PNG)
> 
> Now we have to create a table where, whenever we add `Student` or `Teacher` in to the Database it will automatically reflect to that permaculture Database
> 
> Before doing that we have to import the following Library
> 
```commandline
from django.db.models.signals import post_save
from django.dispatch import receiver
```
> 
> The Code and instruction are given in the following 
> 
```commandline
@receiver(post_save, sender=Student)                                # Method to add Student in to the student Table
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'STUDENT':
        StudentProfile.objects.create(user=instance)                # By this Student Data will Store in to Student Table


class StudentProfile(models.Model):     # Table for Student
    user = models.OneToOneField(User, on_delete=models.CASCADE) 
    student_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user                # By This the name of the Student will Reflect to the Admin page

```
> 
> You are all Set. Now copy and paste the following Commend
> 
```commandline
python manage.py makemigrations
python manage.py migrate
```
>
> Now lets how the Database looks like 
> 
> ![StudentData](../Screen%20Shots/ss13.PNG)
> 
> ![StudentData](../Screen%20Shots/ss14.PNG)
> 
> Before updating it to Admin Page copy & paste the following code to the `User/admin.py` file
```commandline
from .models import *

admin.site.register(StudentProfile)
```
> 
> This is how it looks like from Admin Section
> 
> ![DjangoAdmin](../Screen%20Shots/ss15.PNG)
> 
> That's all for Step 4. Let's move on to Step 5
> 