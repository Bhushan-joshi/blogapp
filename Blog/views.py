from django.shortcuts import render ,redirect
from .models import Post
from django.views.generic import  ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def index(request):
    Data={
        'udata':Post.objects.all(),
    }
    return render(request,'index.html' ,Data)

class PostList(ListView):
    model=Post
    template_name = "index.html"
    context_object_name='udata'
    ordering=['-date_posted']

class Postdetail(DetailView):
    model=Post
    DetailView.model=Post
    DetailView.queryset=Post.objects.all()
    # template_name="post_detail.html"
    
class CreatePost(LoginRequiredMixin,CreateView):
    login_url="login"
    CreateView.module=Post
    fields=['title','post_data']
    CreateView.queryset=Post.objects.all()
    template_name = "Blog/post_form.html"

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class UpdatePost(UserPassesTestMixin,LoginRequiredMixin,UpdateView):
    login_url="login"
    UpdateView.module=Post
    fields=['title','post_data']
    UpdateView.queryset=Post.objects.all()
    template_name = "Blog/post_form.html"

    def form_valid(self, form):
        form.instance.author=self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

class DeletePost(UserPassesTestMixin,LoginRequiredMixin,DeleteView):
    model=Post
    DetailView.model=Post
    DetailView.queryset=Post.objects.all()
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user==post.author:
            return True
        return False

def about(request):
    return render(request,'about.html')

