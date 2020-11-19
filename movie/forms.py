from .models import Post
from django import forms 


class CommentForm(forms.Form):
    class Meta:
        model = Post
        fields = (' num_user','note','datecrea')