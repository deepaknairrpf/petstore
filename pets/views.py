from django.shortcuts import render
from rest_framework import viewsets
from pets.models import Pet
from pets.serializers import PetSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class PetsViewSet(viewsets.ModelViewSet):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('name', 'species', 'country_of_origin', 'owner__username')
    search_fields = ('name', 'species', 'country_of_origin', 'owner__username')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
