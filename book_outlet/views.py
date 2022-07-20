from django.shortcuts import render
from . import models


def index(request):
    return(render(request, "book_outlet/index.html",{
        "books" : models.Book.objects.all()
    }))
