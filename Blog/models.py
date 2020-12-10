from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published'),
    )
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=250, unique=True)
    slug = models.SlugField(max_length=250, unique=True)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,related_name='blog_posts')
    complain_compliment_user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE ,related_name='blog_complain')
    published = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default=0)
    complain = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE ,related_name='Comment')
    user = models.CharField(max_length=250)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    complain = models.BooleanField(default=False)

    def approved(self):
        self.approved = True
        self.save()

    def __str__(self):
        return self.user