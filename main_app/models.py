from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class City(models.Model):
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=200)
    country = models.CharField(max_length=75)

    def __str__(self):
            return self.name

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=150)
    image = models.CharField(max_length=250)
    
    def __str__(self):
       return f"{self.user.first_name} {self.user.last_name}"
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=600)
    image = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()

    def __str__(self):
            # return f"Posted: {self.post_date} - Post Title: {self.title} - Author: {self.user.first_name}, posted an article about {self.city.name}."
            return f"{self.title}"
    class Meta:
        ordering = ['-post_date']


