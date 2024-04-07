from django.http import JsonResponse

from .models import Book


def book_detail(book_id):
    book = Book.objects.get(pk=book_id)
    data = {
        'name': book.name,
        'page_count': book.page_count,
        'category': book.category,
        'author_name': book.author_name,
        'price': str(book.price),
        'image_url': book.image.url if book.image else None
    }
    return JsonResponse(data)
