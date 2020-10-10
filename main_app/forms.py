from django.forms import ModelForm
from .models import Image, Post, User_Profile

class Image_Form(ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
        
class User_Form(ModelForm):
    class Meta:
        model = User_Profile
        fields = ['user_name', 'user_city', 'join_date', 'post']

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = [
            'post_title', 'post_city','post_content', 'user' 
        ]