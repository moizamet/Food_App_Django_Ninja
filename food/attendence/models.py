from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

#basic its and sabeel
class App_Custom_User(AbstractUser):
    username=models.CharField(max_length=500,unique=True)
    name=models.CharField(max_length=1000)
    its=models.CharField(max_length=20,unique=True)
    sabeel=models.CharField(max_length=100)
    email=models.EmailField(default=None)
    phone_number=models.CharField(max_length=15)
    custom_comments=models.TextField()
    role=models.CharField(max_length=2000,default="User")

    USERNAME_FIELD="username"

    def __str__(self):       
        return self.username

class Venue(models.Model):
    name=models.CharField(max_length=3000)
    address=models.TextField()
    contact_name=models.CharField(max_length=1000,default=None)
    contact_number=models.CharField(max_length=20,default=None)
    active=models.BooleanField(default=True)

class Miqaat(models.Model):
    title=models.CharField(max_length=2000)
    information=models.TextField()
    venue=models.ForeignKey(Venue,on_delete=models.CASCADE)
    is_capacity_required=models.BooleanField(default=False)
    capacity=models.IntegerField(default=0)
    date=models.DateTimeField()
    cutoff_date=models.DateTimeField()
    creator=models.ForeignKey(App_Custom_User,  on_delete=models.CASCADE)
    active=models.BooleanField(default=True)

class Miqaat_Registration(models.Model):
    miqaat=models.ForeignKey(Miqaat,on_delete=models.CASCADE)
    sabeel_id=models.CharField(max_length=100)
    user_count=models.IntegerField(default=1)
    date=models.DateTimeField(auto_now_add=True)
