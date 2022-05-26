from django import  forms
from theory.models import  Post


class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields=['title', 'text', 'author', 'status']
