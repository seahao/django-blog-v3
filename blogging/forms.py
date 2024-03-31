from django import forms
from blogging.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "text"]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
