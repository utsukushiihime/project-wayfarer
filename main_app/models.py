from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class Image(models.Model):
    name= models.CharField(max_length=500)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)


class Post(models.Model):
    post_title = models.CharField(max_length=200)
    post_city = models.CharField(max_length=75)
    post_content = models.TextField(max_length=600)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

def __str__(self):
        return self.user

class City(models.Model):
    name = models.CharField(max_length=75)

def __str__(self):
        return self.user


class Profile(models.Model):
    name = models.CharField(max_length=150)
    user_city = models.CharField(max_length=150)
    join_date = models.DateField('Join Date')
    post = models.ManyToManyField(Post)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
