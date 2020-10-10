from django.db import models
from django.contrib.auth.models import User

# # Create your models here.
class City(models.Model):
    name = models.CharField(max_length=75)
    image = models.CharField(max_length=200)
    country = models.CharField(max_length=75)

def __str__(self):
        return f"{self.name}, {self.country}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    current_city = models.ForeignKey(City, on_delete=models.CASCADE)
    image = models.CharField(max_length=250)
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=600)
    image = models.CharField(max_length=300)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post_date = models.DateField()

    def __str__(self):
            return f"{self.user} = {self.city.name} Post: {self.title} created:{self.post_date} \n{self.content}"
    class Meta:
        ordering = ['-post_date']