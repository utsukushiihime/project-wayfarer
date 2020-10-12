from django.db.models.fields import CharField
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Profile, City, Post

    
class Register_Form(UserCreationForm):
    
    current_city = forms.CharField(required=True)
    
    class  Meta: 
        model = User
        fields = ('username', 'password1', 'password2', 'current_city')

    def save(self, commit=True):
        user = super(Register_Form, self).save(commit=False)
        user.current_city = self.cleaned_data["city"]
        if commit:
            user.save()
        return user
        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','city', 'image']
        
class Register_Form(UserCreationForm):
    city = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100, help_text='Username')

    class Meta:
        model = User
        fields = ["username", "password1", "password2", "city", "email", "first_name", "last_name"]
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
        'city': forms.TextInput(
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

        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['city', 'image']

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