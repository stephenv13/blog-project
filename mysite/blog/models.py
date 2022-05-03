from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.

'''
There are two models for the blog store in SQL:
    - Post
    - Comments
'''
# create blog post
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    published_date = models.DateTimeField(blank=True,null=True)

    # publish blog post
    def publish(self) -> None:
        self.published_date = timezone.now()
        self.save()

    # approve comment on blog post
    def approve_comments(self):
        return self.comments.filter(approved_comments=True)
    
    # after making blog post, go to url of the new blog post
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    
    # str representation of blog post
    def __str__(self) -> str:
        return self.title

# create comment
class Comment(models.Model):
    post = models.ForeignKey('blog.post',related_name='comments', on_delete=models.DO_NOTHING)
    author = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now())
    approved_comment = models.BooleanField(default=False)

    def approved(self) -> None:
        self.approved_comment = True
        self.save()

    # once user is done writing comment, return to main page
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self) -> str:
        return self.text