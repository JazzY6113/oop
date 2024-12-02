from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic
from django.urls import reverse


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    num_genres = Genre.objects.count()

    search_word = request.GET.get('search_word', '')

    num_books_with_word = Book.objects.filter(title__icontains=search_word).count() if search_word else 0

    return render(
        request,
        'index.html',
        context={
            'num_books': num_books,
            'num_instances': num_instances,
            'num_instances_available': num_instances_available,
            'num_authors': num_authors,
            'num_genres': num_genres,
            'num_books_with_word': num_books_with_word,
            'search_word': search_word,
        },
    )

class BookListView(generic.ListView):
    model = Book
    paginate_by = 2

    def get_queryset(self):
        return Book.objects.filter(title__icontains='')[:5]

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 1

    def get_queryset(self):
        return Author.objects.all()

class AuthorDetailView(generic.DetailView):
    model = Author