from django.urls import path
from .views import (
    ContactListView,
    ContactDetailView,
    ContactListViewWeb,
    ContactDeleteView,
    ContactUpdateView,
    ContactCreateView,
)

urlpatterns = [
    path("", ContactListViewWeb.as_view(), name="contacts-list"),
    path("contacts/", ContactListView.as_view(), name="contact-list"),
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact-detail"),
    path("contacts/<int:pk>/update/", ContactUpdateView.as_view(), name="contact-update"),
    path("contacts/create/", ContactCreateView.as_view(), name="contact-create"),
    path("contacts/<int:pk>/delete/", ContactDeleteView.as_view(), name="contact-delete"),
]
