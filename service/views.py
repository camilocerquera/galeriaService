__author__ = 'jc.cerquera10@uniandes.edu.co'
from service.models import Urls, Contact
from service.serializers import UrlSerialializer, ContactSerializer
from rest_framework import viewsets

# Define el comportamiento de la vista

class UrlsViewSet(viewsets.ModelViewSet):
    queryset = Urls.objects.all().order_by('-date')
    serializer_class = UrlSerialializer

class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
