from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class Register_Form(UserCreationForm):
    first_name = forms.Charfield()
    last_name = forms.CharField()
    email = forms.EmailField()
    current_city = forms.ModelChoiceField(queryset=City.objects.all())
    
    class  Meta: 
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'current_city']
        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','first_name', 'last_name', 'current_city', 'post', 'image']

class Post_Form(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title', 'city','content', 'user', 'post_date' 
        ]
        
class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'image', 'country']
        
class Image_Form(ModelForm):
    class Meta:
        model= Image
        fields= ['name', 'imagefile']