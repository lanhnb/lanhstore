from django.contrib import admin
from .models import Contact, Post, Comment, KM
# Register your models here.
class PostAdmin( admin.ModelAdmin ):
    list_display = ['title']
    list_filter = ['date']

class CommentInline(admin.StackedInline):
    model = Comment

admin.site.register(Contact)
admin.site.register(KM)


@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject1.js',)