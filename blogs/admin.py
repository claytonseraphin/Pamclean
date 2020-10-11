from django.contrib import admin
from .models import Blogs
# Register your models here.

class BlogsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Blogs, BlogsAdmin)
