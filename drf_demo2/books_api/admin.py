from django.contrib import admin
from drf_demo2.books_api.models import Book


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass
