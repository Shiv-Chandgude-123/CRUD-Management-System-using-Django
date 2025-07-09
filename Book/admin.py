from django.contrib import admin

from .models import book,employee

# Register your models here.
admin.site.register(book)
admin.site.register(employee)