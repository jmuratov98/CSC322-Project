from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from models import Comment
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
			return redirect('blog:post_detail')
	else:
		form = CommentForm()
	template = 'Blog/post/add_comment.html'
	context = {'form': form}
	return render(request, template, context)


	def taboo_censor(request)
		item = Comment.objects.get(post,body)
		swag = Post.objects.get(title, content)
    	if __name__ == "__main__":
        	profanity.load_censor_words()

        	postvar = item.post
			postvar = profanity.censor(postvar)  
			bodyvar = item.body
			bodyvar = profanity.censor(bodyvar)     
			titlevar = swag.title
			titlevar = profanity.censor(titlevar)
			contentvar = swag.content
			contentvar = profanity.censor(contentvar)



def taboo_checker(request)
   
    if __name__ == "__main__":
        text = #Once Blog Implemented, string of text that gets submitted will be scanned here

        if profanity.contains_profanity(text)= True
            Users.warnings += 1
    
            