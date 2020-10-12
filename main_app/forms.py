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
        user = super(Register_Form, self).save(commit)
        user.current_city = self.cleaned_data["current_city"]
        if commit:
            user.save()
        return user



        
class User_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['user','current_city', 'image']
        
class Profile_Form(ModelForm):
    class Meta:
        model = Profile
        fields = ['current_city']

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