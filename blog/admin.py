from django.contrib import admin
from .models import BlogPost,Comment,Like


class CommentInLine(admin.TabularInline):
	model = Comment
	extra =1

class LikeInLine(admin.TabularInline):
	model = Like
	extra = 1

class BlogPostAdmin(admin.ModelAdmin):
	inlines =[
		CommentInLine,
		LikeInLine
	]
from rest_framework.authtoken.admin import TokenAdmin

TokenAdmin.raw_id_fields = ['user']

admin.site.register(BlogPost,BlogPostAdmin)
admin.site.register(Comment) 
admin.site.register(Like)
