from django.shortcuts import render
from rest_framework import viewsets
from .serializer import RestSerializer
from .models import Rest
# from rest_framework.views import APIView


class Home(viewsets.ModelViewSet):
    queryset = Rest.objects.all()
    serializer_class = RestSerializer


