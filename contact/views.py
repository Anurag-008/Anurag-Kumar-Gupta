from warnings import filters
from django.shortcuts import render
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from .serializer import contact_serializer
from .models import contact
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

# Create your views here.

# Listing contacts
class list_contact_view(ListAPIView):
    queryset = contact.objects.all()
    serializer_class = contact_serializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['=name', 'email']
    pagination_class = PageNumberPagination
    authentication_class = [BasicAuthentication, SessionAuthentication]
    permission_class = [AllowAny]

# creating contact
class create_contact_view(CreateAPIView):
    queryset = contact.objects.all()
    serializer_class = contact_serializer

# updating contact
class update_contact_view(UpdateAPIView):
    queryset = contact.objects.all()
    serializer_class = contact_serializer

class delete_contact_view(DestroyAPIView):
    queryset = contact.objects.all()
    serializer_class = contact_serializer