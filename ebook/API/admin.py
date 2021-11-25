from django.contrib import admin
from API.models import * 
# Register your models here.

class CategoryView():
    model = Category
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)

admin.site.register(Category)
admin.site.register(Book)