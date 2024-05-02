from django.contrib import admin
from .models import Books

class BooksAdmin(admin.ModelAdmin):
    list_display = ['id','title','author','pages','price']
admin.site.register(Books,BooksAdmin)
