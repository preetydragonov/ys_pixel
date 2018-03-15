from django.urls import path

from . import views

urlpatterns = [
    path('', views.searched_board, name='searched_board'),
]



