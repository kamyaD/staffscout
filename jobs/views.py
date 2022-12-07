from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Jobs
from rest_framework import generics
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from .serializers import JobsSerializer
from .permissions import IsOwnerOrReadOnly

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'snippets': reverse('jobs-list', request=request, format=format)
    })

class JobsCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new jobs
    queryset = Jobs.objects.all(),
    serializer_class = JobsSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class JobsList(generics.ListAPIView):
    # API endpoint that allows jobs to be viewed.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

    
class JobsDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single jobs by pk.
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly]
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class JobsUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a jobs record to be updated.
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer

class JobsDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a jobs record to be deleted.
    queryset = Jobs.objects.all()
    serializer_class = JobsSerializer
