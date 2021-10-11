from django.contrib import admin
from .models import Contact, Post, Comment
# Register your models here.
class PostAdmin( admin.ModelAdmin ):
    list_display = ['title']
    list_filter = ['date']

class CommentInline(admin.StackedInline):
    model = Comment

admin.site.register(Contact)
admin.site.register(Post)
