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






















