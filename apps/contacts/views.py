from django.views.generic import ListView
from rest_framework import generics
from .models import Contact
from .serializers import ContactSerializer

# from drf_yasg.utils import swagger_auto_schema


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


class ContactUpdateView(generics.UpdateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactDeleteView(generics.DestroyAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer


class ContactCreateView(generics.CreateAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
