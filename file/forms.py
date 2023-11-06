from django import forms
from django.contrib.auth.forms import AuthenticationForm
from file.models import Uploadfile


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

# class UploadfilesForm(forms.Form):
#     title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','maxlength':'100','name':'title'}),required=False)
#     file = forms.FileField(widget=forms.FileInput(attrs={'class': 'form-control','name':'file'}),required=False)

    
class UploadfilesForm(forms.ModelForm):
    class Meta:
        model = Uploadfile
        fields = ['title', 'file']
        widgets = {   
        'title': forms.TextInput(attrs={'class': 'form-control','maxlength':'100'}),
        'file':forms.FileInput(attrs={'class': 'form-control','name':'file'})
        }
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'custom-class', 'id': 'title-input'}),
        #     'file': forms.ClearableFileInput(attrs={'class': 'custom-class', 'id': 'file-input'}),
        # }