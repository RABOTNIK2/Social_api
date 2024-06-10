from django import forms
from .models import *

class UserFrom(forms.ModelForm):
    class Meta:
        model = User
        fields = ['login', 'password', 'image', 'email']
        widgets = {
            'email': forms.EmailInput()
        }
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['text', 'image', 'theme']
        
        def __init__(self):
            self.fields['theme'].queryset = Theme.objects.all()
            
            
class ReviewForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'image']