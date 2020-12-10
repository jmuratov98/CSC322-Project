from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,related_name='blog_posts')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.title
