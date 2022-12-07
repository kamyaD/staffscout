from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Candidate
from rest_framework import generics,status
from rest_framework.views import APIView
from .serializers import CandidateSerializer


class CandidateCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new candidate
    queryset = Candidate.objects.all(),
    serializer_class = CandidateSerializer


class CandidateList(generics.ListAPIView):
    # API endpoint that allows candidate to be viewed.
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single candidate by pk.
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a candidate record to be updated.
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class DeclereInterestInAJob(APIView):
    serializer_class = CandidateSerializer

    def post(self, request, format=None):
        pass