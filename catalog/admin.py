from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin class for the Author model."""

    pass


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin class for the Book model."""

    pass


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Admin class for the BookInstance model."""

    pass


admin.site.register(Genre)
admin.site.register(Language)
