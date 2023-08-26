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
> ![Shell](../Screen%20Shots/ss1.PNG)
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
> ![Shell](../Screen%20Shots/ss2.PNG)
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
> ![Shell](../Screen%20Shots/ss3.PNG)
> 
> You can also check the Database at VSCode or DB Browser. Here I am using VSCode. This is How the database looks like
> 
> ![DataBase](../Screen%20Shots/ss5.PNG)
> 
> Here You can see The Default Role is Set as `ADMIN`
> 
> Now The Question is can you Log in as Admin, Lets find out
> 
> ![Admin](../Screen%20Shots/ss6.PNG)
> 
> Clearly You can not Log in as Admin. Now Let's look at this picture
> 
> ![Database](../Screen%20Shots/ss4.PNG)
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
> ![Database](../Screen%20Shots/ss7.PNG)
> Here you can see the `is_superuser` is set as `1`
> 
> ![Database](../Screen%20Shots/ss8.PNG)
> And The Role is also Set as `ADMIN`
> 
> Now You can log in as Admin
> 
> ![Admin](../Screen%20Shots/ss9.PNG)
> 
> ![AdminPage](../Screen%20Shots/ss10.PNG)
> 
> Enough for Step 3, Moving on to Step 4
> 