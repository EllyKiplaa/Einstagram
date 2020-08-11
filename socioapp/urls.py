from django.conf.urls import url,include
from . import views

from .views import(
    PostListView,
    PostCreateView,
)

app_name = "sociaapp"

urlpatterns = [
    #local :
    url(r"^$", PostListView.as_view(), name='post_list'),
    url(r"^new/", PostCreateView.as_view(), name='post_create'),
    
   
]