from django.urls import path
from .views import (BookCreate_API,
                    BookRead_API,
                    SingleBookRead_API,
                    BookUpdate_API,
                    BookDelete_API
                    )

urlpatterns = [
    path('book_create/', BookCreate_API.as_view(), name='book-create'),
    path('book_read/', BookRead_API.as_view(), name='book-read'),
    path('book_single/<int:id>', SingleBookRead_API.as_view(), name='book-single'),
    path('book_update/<int:id>', BookUpdate_API.as_view(), name='book-update'),
    path('book_delete/<int:id>', BookDelete_API.as_view(), name='book-delete'),
]

