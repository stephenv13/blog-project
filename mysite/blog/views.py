from django.utils import timezone
from re import template
from blog.models import Post,Comments
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView)


# Create your views here.

# CLASS BASED VIEWS

# about page
class AboutView(TemplateView):
    template_name = 'about.html'

# post list 'home page'
class PostListView(ListView):
    model = Post

    # SQL query on model, grab the post model and filter by (less than or equal to 'lte'), published date (newest first)
    # FIELD LOOKUPS -> django documentation
    def get_queryset(self):
        # SELECT * FROM Post WHERE published_date <= timezone.now().ect
        return Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')

# post/detail view
class PostDetailView(DetailView):
    model = Post

# create post view
class CreatePostView(LoginRequiredMixin,CreateView):
    # if not logged in.. redirect to login page
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

# update an old post
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'

    form_class = PostForm

    model = Post

# delete post
class PostDeleteView(DeleteView):
    model = Post

    # after a successful delete, return to the home page (post_list)
    success_url = reverse_lazy('post_list')


# unpublished drafts
class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_list.html'

    model = Post

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')