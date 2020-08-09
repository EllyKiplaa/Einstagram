from django.shortcuts import render
from .models import Post
from django.views.generic import(

 listview)


# Create your views here.

class PostListView(ListView):
    template_name = "socioapp/post_list.html"
    queryset = post.objects.all()
    context.object_name ='posts'
