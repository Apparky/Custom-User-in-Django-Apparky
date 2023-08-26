# Custom User in Django Apparky

In this project we design a Django web admin where you can Customise a User Model in Django by defining there role

Here we have selected a Teacher Student model for this example

Following guide are given billow for this project



> # Step-by-Step Guide
>
> ## Step 1:-
> Opem Terminal in your system and type the given commend
> 
```commandline
pip install django
```
> We have attached a `requirement.txt` file with this project you can also install all dependencies with it like this
> 
```commandline
pip install -r requirement.txt
```
> 
> Now type this command on your terminal
```commandline
django-admin stratproject TestUser . ## Your project name can be deferent
```
> By this you are done with creating the project file
> 
> Now Create an App for this project. Commend for that are given billow
> 
```commandline
python manage.py startapp User ## Your App name can be diferent
```
>
> 
> We are done with Step 1
> 
> ## Step 2:
>
> We have created the Project file, and it's App file, Now Connect the App with Project
> 
> Go to `TestUser/settings.py`, You will fine there is a section named `INSTALLED_APPS` like this
> 
```commandline
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]
```
> Change it to like this
> 
```commandline
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    
    "User",
]

```
>
> By doing this we have connected the Project with its App.
> 
> On Next Step we will modify the Default User Model to custom User Model
> 
> ## Step 3:
> 
> Here We will change the User Model 
> 
> Now Go to the `User/model.py` and open the file with your code editor 
> 
> We have to import `AbstrutUser` and `BaseUserManager` 
> 
```commandline
from django.contrib.auth.models import AbstractUser, BaseUserManager

```
> By using `AbstrustUser` you can modify and ad column to the User Table
> 
> Now Copy and Paste the given code
> 
```commandline
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
```
> 
> 
> In This code we have mentioned everything as comment section
> 
> Now let's test if it's working or not
> 
> Go to you native terminal and open django-shell by using this command
```commandline
python manage.py shell
```
>
> A Shell window will open, and you can add Users using that
> 
> This is how a Shell in Terminal looks Like
> 
> ![Shell](Screen%20Shots/ss1.PNG)
> 
> You can add User by following this command
 ```commandline
>>> from User.models import User
>>> User.objects.create_user(username='Apparky', email='apparky@protonemail.com', password='Apparky')
>>> <User: Apparky>
```
>
> This is how it Looks like
> 
> ![Shell](Screen%20Shots/ss2.PNG)
> 
> You can also Check all Users using Shell by following this commend
```commandline
>>> User.objects.all()
<QuerySet [<User: Apparky>]>   # This is user
>>>
```
>
> This is how it looks like
> 
> ![Shell](Screen%20Shots/ss3.PNG)
> 
> You can also check the Database at VSCode or DB Browser. Here I am using VSCode. This is How the database looks like
> 
> ![DataBase](Screen%20Shots/ss5.PNG)
> 
> Here You can see The Default Role is Set as `ADMIN`
> 
> Now The Question is can you Log in as Admin, Lets find out
> 
> ![Admin](Screen%20Shots/ss6.PNG)
> 
> Clearly You can not Log in as Admin. Now Let's look at this picture
> 
> ![Database](Screen%20Shots/ss4.PNG)
> 
> Here You can see the `is_superuser` is set as `0`. This is the reason we can not log in as Admin. For that We have to create a `Super User`
> 
> Let's Create one Super User. Code to create a Superuser is 
> 
```commandline
python manage.py createsuperuser
```
> 
> This is how it works
> 
```commandline
(venv) PS C:...\tests> python manage.py createsuperuser
Username: ShadowKing
Email address: shadowdattablog420@gmail.com
Password:
Password (again):
This password is too short. It must contain at least 8 characters.
This password is too common.
This password is entirely numeric.
Bypass password validation and create user anyway? [y/N]: y
Superuser created successfully.
```
>
> 
> Lets See the Database now
> 
> ![Database](Screen%20Shots/ss7.PNG)
> Here you can see the `is_superuser` is set as `1`
> 
> ![Database](Screen%20Shots/ss8.PNG)
> And The Role is also Set as `ADMIN`
> 
> Now You can log in as Admin
> 
> ![Admin](Screen%20Shots/ss9.PNG)
> 
> ![AdminPage](Screen%20Shots/ss10.PNG)
> 
> Enough for Step 3, Moving on to Step 4
> 
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
> ![StudentShell](Screen%20Shots/ss11.PNG)
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
> ![UserShell](Screen%20Shots/ss12.PNG)
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
> ![StudentData](Screen%20Shots/ss13.PNG)
> 
> ![StudentData](Screen%20Shots/ss14.PNG)
> 
> Before updating it to Admin Page copy & paste the following code to the `User/admin.py` file
```commandline
from .models import *

admin.site.register(StudentProfile)
```
> 
> This is how it looks like from Admin Section
> 
> ![DjangoAdmin](Screen%20Shots/ss15.PNG)
> 
> That's all for Step 4. Let's move on to Step 5
> 
> ## Step 5:
> 
> Let's do the same for `Teacher` profile.
> 
> Copy and Paste the following code for the same 
> 
```commandline
class TeacherManager(BaseUserManager):      # Section to manage User when the role is Teacher
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(role=User.Role.TEACHER)       # Here we have to define the User Role as Teacher


class Teacher(User):
    base_role = User.Role.TEACHER
    teacher = TeacherManager()      # Here we declare The User is a Teacher

    class Meta:
        proxy = True


@receiver(post_save, sender=Teacher)                      # Method to add Teacher in to the Teacher Table
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.role == 'TEACHER':
        TeacherProfile.objects.create(user=instance)        # By this Teacher Data will Store in to Teacher Table 


class TeacherProfile(models.Model):     # Table for Teacher
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    teacher_id = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.user        # By This the name of the Teacher will Reflect to the Admin page
```
> 
> Now Let's migrate the new model by using the given code
```commandline
python manage.py makemigrations
python manage.py migrate
```
> 
> You are all set, New lets try in on python shell
> 
> 
```commandline
>>> from User.models import *
>>>
>>> Teacher.objects.create_user(username='Teacher', email='teacher@gmail.com', password='teacher')
<Teacher: Teacher>              # New User Created as Teacher
>>>
>>>
>>> Teacher.teacher.all()       # Way 1 to see User as Teacher
<QuerySet [<Teacher: Teacher>]> # Teacher List
>>>
>>>
>>>
>>> User.objects.filter(role='TEACHER')     # Way 2 to see User as Teacher
<QuerySet [<User: Teacher>]>    # Teacher List
>>>
>>>
>>> User.objects.all()      # Way to see all Users
<QuerySet [<User: Apparky>, <User: ShadowKing>, <User: AVI>, <User: Teacher>]>  # All User List
>>>

```
>
> This is how it looks like
> 
> ![TeacherShell](Screen%20Shots/ss16.PNG)
> 
> This is how it looks like in Database 
> 
> ![TeacherDatabase](Screen%20Shots/ss17.PNG)
> 
> 1 User has been added as Role `TEACHER` in to the database
> 
> ![TeacherDatabase](Screen%20Shots/ss18.PNG)
> 
> We can also see 1 User has been added to the Teacher Profile as Well
> 
> To display it to the Admin portal add the following code to the `User/admin.py` file
```commandline
admin.site.register(TeacherProfile)
```
>
> This is how it looks like in admin Section
> 
> ![TeacherAdmin](Screen%20Shots/ss19.PNG)
> 
> And we are done with this project 
> 
> Thanks for Your Time
> 
> 
> 
> 
> 
> 
> -------------------
> 
> To get more interesting projects follow our GitHub page at [Here](https://github.com/Apparky)
> 
> To get more interesting projects follow our Bitbucket page at [Here](https://apparky.vercel.app/)
> 
> To know more about [__APPARKY__](https://apparky.vercel.app/) Click [Here](https://apparky.vercel.app/)
























