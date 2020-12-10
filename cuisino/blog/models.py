from django.db import models
from datetime import datetime
from django.urls import reverse
from django.utils.translation import gettext as _
from autoslug.fields import AutoSlugField  #django-autoslug package 
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models.Model):
    class Meta: 
        verbose_name = 'blog post'
        verbose_name_plural = 'blog posts'
        ordering = ['pub_date']             #date post was published

    title = models.CharField(_('title'), max_length=255)
    slug = AutoSlugField(_('slug'), populate_from='title', unique=True)
    image = models.ImageField(_('image'), blank=True, null=True, upload_to='blog')
    text = RichTextField(_('text'))
    description = models.TextField(_('description'), blank=True, null=True)
    published = models.BooleanField(_('published'), default=False)

    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)
    pub_date = models.DateTimeField(_('publish date'), blank=True, null=True)