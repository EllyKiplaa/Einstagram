from django.shortcuts import render,redirect
from .forms import PostForm
from .models import Post
from django.views.generic import(
    ListView,
    CreateView

 )


# Create your views here.

class PostListView(ListView):
    template_name = "/home/elly/Core/Einstagram/socioapp/templates/post_list.html"
    queryset = Post.objects.all()
    context_object_name ='posts'

class PostCreateView(CreateView):
    template = '/home/elly/Core/Einstagram/socioapp/templates/post_create.html'
    from_class = postFrom
    querset = post.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        form.instance.auther = self.request.user

        return super().form_valid(form)