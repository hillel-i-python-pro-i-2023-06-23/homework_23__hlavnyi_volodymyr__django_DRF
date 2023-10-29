from django.views.generic import ListView
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer


class ContactListView(generics.ListCreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactListViewWeb(ListView):
    model = Contact
    context_object_name = "contacts_list"
    template_name = "contacts/contacts_list.html"


class ContactDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
