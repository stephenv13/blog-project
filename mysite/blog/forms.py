from django import forms
from blog.models import Post,Comments

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
        model = Comments
        fields = ('author','text')

        widgets = {
            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }