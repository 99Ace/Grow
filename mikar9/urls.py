from django.urls import path, include
from .views import mikar9, add, show, delete, edit, view_account, sorter

urlpatterns = [
    path('', mikar9, name='mikar9'),
    path('add', add, name='add'),
    path('edit/<item_id>', edit, name='edit'),
    path('show', show, name='show'),
    path('view_account', view_account, name='view_account'),
    path('sorter', sorter, name='sorter'),
    path('delete/<item_id>', delete, name='delete'),
]
