from django.conf.urls import path, include
# from django.conf import settings
# from django.conf.urls.static import static
# from django.views.static import serve
from django.urls import path

from .views import(
    PostListView,
    PostCreateView,
)

app_name = "sociaapp"

urlpatterns = [
    #local :
    path("", PostListView.as_view(), name='post_list'),
    path("/new", PostCreateView.as_view(), name='post_create'),
    
    # path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    # path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 