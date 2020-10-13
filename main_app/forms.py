from django.db.models.fields import CharField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, City, Post

    
class Register_Form(UserCreationForm):
    
    class Meta:
        model = User
        fields = ["username", "password1", "password2", "email", "first_name", "last_name"]
        widgets = {
        'username': forms.TextInput(
            attrs={
                'class': 'form-control'
                }
            ),
        'password1': forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
            ),
        'password2': forms.PasswordInput(
            attrs={
                'class': 'form-control'
                }
            ),
        'email': forms.EmailInput(
            attrs={
                'class': 'form-control'
            }
            ),
        'first_name': forms.TextInput(
            attrs={
                'class': 'form-control'
            }
            ),
        'last_name': forms.TextInput(
            attrs={
                'class': 'form-control'
            }
            ),
        
        }

        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','city', 'image']
        
        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'image']

class User_Form(ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name']

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