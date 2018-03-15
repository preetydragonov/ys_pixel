from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.enterance, name='searching_tab_2'),
]
