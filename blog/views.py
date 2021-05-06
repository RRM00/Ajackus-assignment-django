from django.urls import path
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from django.shortcuts import render
from . import views
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin








def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.htm', context)

def about(request):
    return render(request, 'blog/about.htm', {'title':'About'})

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.htm'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.htm'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/post_form.htm'
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/post_form.htm'  
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Post
    success_url ='/'
    template_name = 'blog/post_confirm_delete.htm'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

    

    
    
    

# Create your views here.
