from django.urls import path
from .views import book_detail

urlpatterns = [
    path('book/<int:book_id>/', book_detail, name='book_detail'),
]
