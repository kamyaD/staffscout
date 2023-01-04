from django.shortcuts import render


from django.shortcuts import render
from rest_framework.response import Response 
from rest_framework import generics,status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import CandidateSerializer,CandidateJobApplicationSerializer
# from jobs.serializers import CandidateJobsInterestedIn
from .models import Candidate,CandidateJobApplication
# from jobs.permissions import IsOwnerOrReadOnly
from jobs.models import Jobs


class CandidateCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new candidate
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidate.objects.all(),
    serializer_class = CandidateSerializer
    

class CandidateList(generics.ListAPIView):
    # API endpoint that allows candidate to be viewed.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single candidate by pk.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a candidate record to be updated.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

class CandidateDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a customer record to be deleted.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer


class CreateCandidateJobApplication(generics.CreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CandidateJobApplication.objects.all()
    serializer_class = CandidateJobApplicationSerializer

class ListCandidateJobApplication(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = CandidateJobApplication.objects.all()
    serializer_class = CandidateJobApplicationSerializer
    



