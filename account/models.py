from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, verbose_name = 'User Object') 
    email_address = models.CharField(max_length=60, unique=True, null=True)
    bio = models.TextField(blank=True, null=True)  
    profile_img = models.ImageField(upload_to='profile_images', default='user.png', blank=True, null=True, verbose_name='Profile Pic')
    location=models.CharField(max_length=100, blank=True, null=True)
    GENDER = (
        ('Female', 'Female'),
        ('Male', 'Male'),
        ('Other', 'Other'),
    )
    gender = models.CharField(max_length=15, choices=GENDER, blank=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    @property
    def full_name(self):
        return f"{self.user.first_name} {self.user.last_name}"