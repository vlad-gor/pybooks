from django.contrib import admin

# Register your models here.
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','year','publisher','link')
    search_fields = ['year']

# Register your models here.
admin.site.register(Book,BookAdmin)