from django.urls import path
from . import views


urlpatterns = [
    path('',views.index, name="index"),
    path('<int:id>/', views.book_detail, name="book_detail")
]
