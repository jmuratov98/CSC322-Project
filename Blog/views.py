from django.shortcuts import render
from .models import Post

def list_of_post(request):
	post = Post.objects.all()
	template = 'Blog/post/list_of_post.html'
	context = {'post': post}
	return render(request, template, context)