from django import forms

class ImageForm(forms.ModelForm):
    class Meta:
        model= Image
        fields= ["name", "imagefile"]
