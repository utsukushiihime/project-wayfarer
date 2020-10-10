from django.forms import ModelForm
from .models import Image, Post, Profile

class Image_Form(ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'user_city', 'join_date', 'post', 'image']

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title', 'post_city','post_content', 'user' 
        ]