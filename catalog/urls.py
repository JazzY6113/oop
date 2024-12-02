from django.urls import path
from . import views
from .views import BBLogoutView, AllLoanedBooksListView

urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('book/<int:pk>/', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', views.AuthorDetailView.as_view(), name='author-detail'),
    path('accounts/logout/', BBLogoutView.as_view(), name='logged_out'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path('all-loaned-books/', AllLoanedBooksListView.as_view(), name='all-borrowed-books'),
]