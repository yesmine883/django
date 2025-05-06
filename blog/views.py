from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.urls import reverse_lazy

class PostList(ListView):
    model = Post
    template_name = 'blog/post_list.html'

class PostDetail(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostUpdate(UpdateView):
    model = Post
    fields = ['title', 'slug', 'author', 'content', 'status', 'image']
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

class PostDelete(DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

