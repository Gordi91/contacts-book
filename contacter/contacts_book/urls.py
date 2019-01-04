from django.urls import path
from  contacts_book import views

urlpatterns = [
    path('', views.Menu.as_view(), name='menu'),
]