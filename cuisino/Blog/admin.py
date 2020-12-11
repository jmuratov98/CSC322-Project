from django.contrib import admin
from Blog.models import Post, Comment

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
	list_display = ('user', 'email')

admin.site.register(Comment, CommentAdmin)