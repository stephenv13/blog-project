from django import forms
from blog.models import Post,Comment

'''
There are two forms on the blog:
    - Blog Post Form
    - Blog Comment F
'''
# widgets inside of the Meta() class make the form editable by CSS styling


class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','title')


        widgets = {
            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),
        }

class CommentForm(forms.ModelForm):
    
    class Metal():
        model = Comment
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }