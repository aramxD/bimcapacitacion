from django.contrib import admin
from .models import *
# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'user') #visualizar columnas

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title') #visualizar columnas

class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'featured', 'timestamp') #visualizar columnas

admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)