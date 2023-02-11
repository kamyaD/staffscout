from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .models import User
from candidate.models import Profiles
from .serializers import UserSerializer, RegisterSerializer
from candidate.serializers import ProfilesSerializer



class UserViewSet(generics.ListAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['is_candidate', 'is_employer','is_both_employer_and_candidate']
    
class UserDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single jobs by pk.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a jobs record to be updated.
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserLogin(ObtainAuthToken):
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, 
        context={
            'request':request
        })
        
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        print("user===>", user)
        # profile = serializer.validated_data['profile_data']
        token = Token.objects.get(user=user)

        return Response({
            'token': token.key,
            'id': user.pk,
            'username': user.username,
            'profilePic': user.profile_pic,
            'email': user.email,
            'isCandidate': user.is_candidate,
            'isBothEmployerAndCandidate':user.is_both_employer_and_candidate,
            'isEmployer': user.is_employer,
            'jobTitle': user.profile.job_title,
        })

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


