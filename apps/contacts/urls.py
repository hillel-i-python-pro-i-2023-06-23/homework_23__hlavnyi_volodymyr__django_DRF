from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import (
    ContactListView,
    ContactDetailView,
    ContactListViewWeb,
    ContactDeleteView,
    ContactUpdateView,
    ContactCreateView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Contacts API",
        default_version="v1",
        description="API for managing contacts",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="vladimir.glavnyy@consultingservices.com.ua"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("", ContactListViewWeb.as_view(), name="contacts-list"),
    path("contacts/", ContactListView.as_view(), name="contact-list"),
    path("contacts/<int:pk>/", ContactDetailView.as_view(), name="contact-detail"),
    path("contacts/<int:pk>/update/", ContactUpdateView.as_view(), name="contact-update"),
    path("contacts/create/", ContactCreateView.as_view(), name="contact-create"),
    path("contacts/<int:pk>/delete/", ContactDeleteView.as_view(), name="contact-delete"),
    #
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]
