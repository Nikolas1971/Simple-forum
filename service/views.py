import imp
from django.shortcuts import render
from service.models import Post, Comment
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .forms import PostForm, CommentForm, UserRegisterForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

def index(req):
    return render(req, 'index.html')

def about(req):
    return render(req, 'about.html')

class RegisterForm(CreateView):
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class PostsView (ListView):
    model = Post
    template_name = 'index.html'
    ordering = ['-created_at']

class DetailPostsView (DetailView):
    model = Post
    template_name = 'detail_post.html' 

class CreatePostsView (PermissionRequiredMixin, CreateView):
    permission_required = 'service.add_post'
    login_url = 'login'
    model = Post
    template_name = 'create_post.html' 
    form_class = PostForm

class UpdatePostsView (PermissionRequiredMixin, UpdateView):
    permission_required = 'service.change_post'
    login_url = 'login'
    model = Post
    template_name = 'create_post.html' 
    form_class = PostForm

class DeletePostsView (PermissionRequiredMixin, DeleteView):
    permission_required = 'service.delete_post'
    login_url = 'login'
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('index')

class AddCommentView (LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Comment
    template_name = 'add_comment.html'
    form_class = CommentForm
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
