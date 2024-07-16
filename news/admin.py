from django.contrib import admin

# Register your models here.
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'published_date')
    fields = ('title', 'text', 'published_date')

admin.site.register(Post, PostAdmin)