from django.urls import path
from drf_demo2.books_api.views import ListBookView, DetailBookView

urlpatterns = [
    path('books/', ListBookView.as_view()),
    path('books/<int:id>', DetailBookView.as_view()),
]


# http://127.0.0.1:8000/api/books/
# http://127.0.0.1:8000/api/books/1
