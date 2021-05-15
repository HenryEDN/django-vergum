from django.forms import ModelForm, TextInput, Textarea, widgets
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Profile

class RegUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')      
        widgets = {
            'username': TextInput(attrs={

            }),
            'email': TextInput(attrs={

                'type': 'email'
            }),
            'password1': TextInput(attrs={

                'type': 'password'
            }),
            'password2': TextInput(attrs={

                'type': 'password'
            })
        }


class UserLoginForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ('username', 'password')  
        widgets = {
            'username': TextInput(attrs={
            }),
            'password': TextInput(attrs={
                'type': 'password'
            })
        }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': Textarea(attrs={
                'placeholder': 'Type comment',
                'class': "form-control", 
                'id': "exampleFormControlTextarea1",
                'rows':6, 
                'cols':50,
                'resize': 'none',
            }),
        }


class ProfileEditForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('nickname', 'about_user', "profile_picture")
        widgets = {
            'nickname': TextInput(attrs={
                'placeholder': 'Type title',
                'class': "form-control",
            }),
            'about_user': Textarea(attrs={
                'placeholder': 'Tell about yourself!',
                'class': "form-control", 
                'id': "exampleFormControlTextarea1",
                'rows':6, 
                'cols':50,
                'resize': 'none',
            }),
        }