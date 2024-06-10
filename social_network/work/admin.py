from django.contrib import admin
from .models import *

admin.site.register(Theme)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['login', 'password']
    
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'posted_by']
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['written_by', 'written_to']

# Register your models here.
