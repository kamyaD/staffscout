from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



from .models import Jobs,Specialisms,Specialities,ContractTypes,EducationLevels
from .serializers import JobsSerializer,SpecialismsSerializer,SpecialitiesSerializer,ContractTypesSerialiers,EducationLevelsSerialiers
from .permissions import IsOwnerOrReadOnly

class JobsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new jobs
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all(),
    serializer_class = JobsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JobsList(generics.ListAPIView):
    # API endpoint that allows jobs to be viewed.
    # permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    
class JobsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single jobs by pk.
    # permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class JobsUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a jobs record to be updated.
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class JobsDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a jobs record to be deleted.
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class SpecialismsList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Specialisms.objects.all()
    serializer_class = SpecialismsSerializer

class SpecialitiesList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Specialities.objects.all()
    serializer_class = SpecialitiesSerializer

class ContractTypesList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = ContractTypes.objects.all()
    serializer_class = ContractTypesSerialiers

class EducationLevelsList(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = EducationLevels.objects.all()
    serializer_class = EducationLevelsSerialiers





  
