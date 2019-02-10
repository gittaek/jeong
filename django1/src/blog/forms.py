from .models import Post
from django import forms

class PostForm(forms.ModelForm):
    file = forms.FileField(required=False, widget=forms.ClearableFileInput(attrs={'multiple':True}))
    image = forms.ImageField(required=False, widget=forms.ClearableFileInput(attrs={'multiple':True}))
    class Meta:
        model = Post
        fields = ['category', 'headline', 'content']