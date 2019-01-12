from django.urls import path
from contacts_book import views

urlpatterns = [
    path('', views.ShowPeople.as_view(), name='show_people'),
    path('new', views.NewPerson.as_view(), name='new_person'),
    path('modify/<int:id>/', views.ModifyPerson.as_view(), name='modify_person'),
    path('delete/<int:id>/', views.DeletePerson.as_view(), name='delete_person'),
    path('show/<int:id>/', views.ShowPerson.as_view(), name='show_person'),
    path('<int:id>/addAddress/', views.AddAddress.as_view(), name='add_address'),
    path('<int:id>/addPhoneNumber/', views.AddPhoneNumber.as_view(), name='add_phone_number'),
    path('<int:id>/addEMail/', views.AddEMail.as_view(), name='add_email'),
    path('newGroup/', views.NewGroup.as_view(), name='new_group'),
    path('modify-group/<int:id>/', views.ModifyGroup.as_view(), name='modify_group'),
    path('show-groups/', views.ShowGroups.as_view(), name='show_groups'),
    path('group/<int:id>/', views.ShowGroup.as_view(), name='show_group'),
    path('delete-group/<int:id>/', views.DeleteGroup.as_view(), name='delete_group'),
    path('delete_person_from_group/<int:group_id>/<int:person_id>/',
         views.DeletePersonFromGroup.as_view(),
         name='delete_person_from_group'),
    path('delete_email_from_person/<int:email_id>/<int:person_id>/',
         views.DeleteEmailFromPerson.as_view(),
         name='delete_email_from_person'),
    path('delete_phone_from_person/<int:phone_id>/<int:person_id>/',
         views.DeletePhoneFromPerson.as_view(),
         name='delete_phone_from_person'),
    path('group-members/<int:id>/', views.GroupMembers.as_view(), name='group_members'),
]
