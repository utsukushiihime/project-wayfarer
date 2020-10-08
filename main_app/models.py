from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class User_Profile(models.Model):
    user_name = models.CharField(max_length=150)
    user_city = models.CharField(max_length=150)
    join_date = models.DateField('Join Date')
    post_title = models.CharField(max_length=200)
    post_city = models.CharField(max_length=75)
    post = models.TextField(max_length=600)


# class Image(models.Model):
#     name= models.CharField(max_length=500)
#     videofile= models.FileField(upload_to='images/', null=True, verbose_name="")

#     def __str__(self):
#         return self.name + ": " + str(self.imagefile)


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_content = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)




