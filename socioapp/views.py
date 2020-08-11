from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.utils import timezone 
from django.views.generic import(
    ListView,
    CreateView,
    DetailView

 )


# Create your views here.

class PostListView(ListView):
    template_name = "/home/elly/Core/Einstagram/socioapp/templates/post_list.html"
    queryset = Post.objects.all()
    context_object_name ='posts'

class PostCreateView(CreateView):
    template_name = '/home/elly/Core/Einstagram/socioapp/templates/post_create.html'
    form_class = PostForm
    querset = Post.objects.all()
    success_url ='/'

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostDetailView(DetailView):

    queryset = Post.objects.all()