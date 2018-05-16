from django import forms
from myApp.models import Blog

class BlogForm(forms.ModelForm):
    
    class Meta:
        model = Blog
        fields = ('poster','postname','post')



