from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'bio', 'profile_pic', 'city', 'country', 'job_title', 'availability_status')
        read_only_field = ('username',)
