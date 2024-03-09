from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model
# Create your models here.
class customUser(AbstractUser):
    profile_pic=models.ImageField(upload_to='profile_pics/',blank=True)
    is_patient=models.BooleanField(default=True)
    is_doctor=models.BooleanField(default=False)
    address_line1=models.CharField(max_length=250)
    city=models.CharField(max_length=250)
    state=models.CharField(max_length=250)
    pincode=models.IntegerField(default=0)


customUser._meta.get_field('groups').remote_field.related_name = 'custom_user_groups'
customUser._meta.get_field('user_permissions').remote_field.related_name = 'custom_user_permissions'

class Patient(models.Model):
    user=models.OneToOneField(customUser,on_delete=models.CASCADE)


class Doctor(models.Model):
    user=models.OneToOneField(customUser,on_delete=models.CASCADE)

class BlogPost(models.Model):
    CATEGORY_CHOICES = [
        ('Mental Health', 'Mental Health'),
        ('Heart Disease', 'Heart Disease'),
        ('Covid19', 'Covid19'),
        ('Immunization', 'Immunization'),
        # Add more categories as needed
    ]

    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='blog_images/', null=True, blank=True)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    summary = models.TextField()
    content = models.TextField()
    author = models.ForeignKey(customUser, on_delete=models.CASCADE)
    is_draft = models.BooleanField()

    def __str__(self):
        return self.title





