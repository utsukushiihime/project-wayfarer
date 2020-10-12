from django.db.models.fields import CharField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, City, Post

class Register_Form(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    current_city = forms.ModelChoiceField(queryset=City.objects.all())
    
    class  Meta: 
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'current_city']
        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','current_city', 'image']
        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'current_city', 'image']

class Post_Form(ModelForm):

    class Meta:
        model = Post
        fields = [
            'title', 'city','content', 'image', 'user', 'post_date' 
        ]
        widgets = {
            'title': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'content': forms.Textarea(
				attrs={
					'class': 'form-control'
					}
				),
            'post_date': forms.TextInput(
				attrs={
					'class': 'form-control'
					}
				),
            'image': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
			}
        
class City_Form(ModelForm):
    class Meta:
        model = City
        fields = ['name', 'image', 'country']