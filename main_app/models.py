from django.db import models
django.contrib.auth.models import User

# Create your models here.

class User_Name(models.Model):
    user_name = models.CharField(max_length=150)
    user_city = models.CharField(max_length=150)
    join_date = models.DateField('Join Date')
    post_title = models.CharField(max_length=200)
    post = models.TextField(max_length=600)
    photo 