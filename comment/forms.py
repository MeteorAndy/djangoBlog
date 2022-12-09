from django import forms
from .models import Comment

# 谢明月
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
