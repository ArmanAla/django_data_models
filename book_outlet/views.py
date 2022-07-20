from django.shortcuts import render
from .models import Book


def index(request):
    return(render(request, "book_outlet/index.html",{
        "books" : Book.objects.all()
    }))
