from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey("auth.User",on_delete.CASCADE)
    image = models.ImageField(blank=True, null=True)
    caption = models.models.TextField()
    create_date = model.DateTime(default=timezone.now)
