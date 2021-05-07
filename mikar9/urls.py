from django.urls import path, include
from .views import mikar9, add, show

urlpatterns = [
    path('', mikar9, name='mikar9'),
    path('add', add, name='add'),
    path('show', show, name='show'),
]