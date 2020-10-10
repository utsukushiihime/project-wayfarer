from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class City(models.Model):
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=200)
    country = models.CharField(max_length=75)

def __str__(self):
        return f"{self.name}, {self.country}"
class Image(models.Model):
    name= models.CharField(max_length=500)
    imagefile= models.FileField(upload_to='images/', null=True, verbose_name="")

    def __str__(self):
        return self.name + ": " + str(self.imagefile)

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=600)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()

def __str__(self):
        return self.user

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_city = models.ForeignKey(City, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

