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