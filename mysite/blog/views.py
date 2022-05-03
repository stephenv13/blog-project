from django.shortcuts import render,get_object_or_404,redirect
from django.utils import timezone
from re import template
from blog.models import Post,Comment
from blog.forms import PostForm,CommentForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
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

################################################

@login_required
def add_comment_to_post(request,pk):
    # get post object or 404 page if not found
    post = get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        form = CommentForm(request.Post)

        # if the form is valid, save the form to the post. Othewise, return back to comment form
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail',pk=post.pk)
    else:
        form = CommentForm()
    return render(request,'blog/comment_form.html',{'form':form})


@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    comment.approved()

    return redirect('post_detail',pk=comment.post.pk)

@login_required
def comment_remove(request,pk):
    comment = get_object_or_404(Comment,pk=pk)
    post_pk = comment.post.pk
    comment.delete()

    return redirect('post_detail',pk=post_pk)

@login_required
def post_publish(request,pk):
    post = get_object_or_404(Post,pk=pk)
    post.publish
    return redirect('post_detail',pk=pk)

