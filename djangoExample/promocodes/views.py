from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import viewsets

from djangoExample.promocodes.models import Promocode
from djangoExample.promocodes.serializers import PromocodeSerializer
from rest_framework import generics


class PromocodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer

class PromocodeListCreate(generics.ListCreateAPIView):
    queryset = Promocode.objects.all()
    serializer_class = PromocodeSerializer
