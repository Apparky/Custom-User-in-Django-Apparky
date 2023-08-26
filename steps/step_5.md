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
> ![TeacherShell](../Screen%20Shots/ss16.PNG)
> 
> This is how it looks like in Database 
> 
> ![TeacherDatabase](../Screen%20Shots/ss17.PNG)
> 
> 1 User has been added as Role `TEACHER` in to the database
> 
> ![TeacherDatabase](../Screen%20Shots/ss18.PNG)
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
> ![TeacherAdmin](../Screen%20Shots/ss19.PNG)
> 
> And we are done with this project 
> 
> Thanks for Your Time
