from django.shortcuts import render
from django.views import generic
from catalog.models import Author, Book, BookInstance, Genre


def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    number_of_books = Book.objects.all().count()
    number_of_book_instances = BookInstance.objects.all().count()
    # Available books (status = 'a')
    number_of_book_instances_available = BookInstance.objects.filter(
        status__exact='a').count()
    # The 'all()' is implied by default
    number_of_authors = Author.objects.count()
    number_of_genres = Genre.objects.count()
    books_match_word = Book.objects.filter(title__contains='the').count()
    context = {
        'books_count': number_of_books,
        'instances_count': number_of_book_instances,
        'instances_available_count': number_of_book_instances_available,
        'authors_count': number_of_authors,
        'genres_count': number_of_genres,
        'books_word_match_count': books_match_word,
    }
    # Render the html template index.html with the data in the context variable
    return render(request, 'catalog/index.html', context=context)


class BookListView(generic.ListView):
    """View class for books page of site."""

    model = Book
    context_object_name = 'book_list'
    queryset = Book.objects.filter(title__icontains='the')[:5]
    paginate_by = 10


class BookDetailView(generic.DetailView):
    """View class for book detail page of site."""

    model = Book


class AuthorListView(generic.ListView):
    """View class for authors page of site."""

    model = Author
    context_object_name = 'author_list'
    queryset = Author.objects.all()
    paginate_by = 5


class AuthorDetailView(generic.DetailView):
    """View class for auhtor detail page of site."""

    model = Author
