from .models import Discussion
from django.forms import ModelForm, TextInput, Textarea, Select

    


class DiscussForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ('title', 'content', 'discussion_topic', 'discussion_picture')
        widgets = {
            'title': TextInput(attrs={
                'placeholder': 'Type title',
                'class': "form-control",
            }),
            'discussion_topic': Select(attrs={
                'class': "btn btn-primary dropdown-toggle"
            }),
            'content': Textarea(attrs={
                'placeholder': 'Type content',
                'class': "form-control", 
                'id': "exampleFormControlTextarea1",
                'rows':10, 
                'cols':50,
                'resize': 'none',
            })
        }
        