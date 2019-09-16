from django.contrib import admin
from .models import Author, Book, BookInstance, Genre, Language


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin class for the Author model."""

    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin class for the Book model."""

    list_display = ('title', 'author', 'display_genre')


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Admin class for the BookInstance model."""

    pass


admin.site.register(Genre)
admin.site.register(Language)
