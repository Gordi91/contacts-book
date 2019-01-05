from django.urls import path
from contacts_book import views

urlpatterns = [
    path('', views.ShowPeople.as_view(), name='show_people'),
    path('new', views.NewPerson.as_view(), name='new_person'),
    path('modify/<int:id>/', views.ModifyPerson.as_view(), name='modify_person'),
    path('delete/<int:id>/', views.DeletePerson.as_view(), name='delete_person'),
    # path('show/<int:id>/'), name='show_person),'

]