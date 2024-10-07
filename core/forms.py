from django import forms
from .models import Creation, Comment

class CreationForm(forms.ModelForm):
    class Meta:
        model = Creation
        fields = ['title', 'description', 'creation_type', 'content', 'tools_used']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']