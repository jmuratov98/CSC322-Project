from django.shortcuts import render, get_object_or_404, redirect
from .models import Post

from .forms import CommentForm

def list_of_post(request):
	post = Post.objects.filter(status='published')
	template = 'Blog/post/list_of_post.html'
	context = {'post': post}
	return render(request, template, context)

def post_detail(request, slug):
	post = get_object_or_404(Post, slug=slug)
	template = 'Blog/post/post_detail.html'
	context = {'post': post}
	return render(request, template, context)

def add_comment(request, slug):
	post = get_object_or_404(Post, slug=slug)
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			comment.post = post
			comment.save()
			return redirect('blog')
	else:
		form = CommentForm()
		template = 'Blog/post/add_comment.html'
		context = {'form': form}
	return render(request, template, context)