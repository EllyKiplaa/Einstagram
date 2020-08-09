from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

from .views import(
    PostListView
)

app_name = "sociaapp"

urlpatterns = [
    #local :
    url("", PostListView.as_view(), name='post_list'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT) 