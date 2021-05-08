from django.urls import path, include
from .views import mikar9, add, show, delete, edit

urlpatterns = [
    path('', mikar9, name='mikar9'),
    path('add', add, name='add'),
    path('edit/<item_id>', edit, name='edit'),
    path('show', show, name='show'),
    path('delete/<item_id>', delete, name='delete'),
]
