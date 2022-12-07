from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Employer
from rest_framework import generics,status
from .serializers import EmployerSerializer


class EmployerCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new customer
    queryset = Employer.objects.all(),
    serializer_class = EmployerSerializer


class EmployerList(generics.ListAPIView):
    # API endpoint that allows customer to be viewed.
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single customer by pk.
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a customer record to be updated.
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer

class EmployerDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Employer.objects.all()
    serializer_class = EmployerSerializer