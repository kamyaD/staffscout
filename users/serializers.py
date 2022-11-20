from django.contrib.auth.models import User, Group
from rest_framework import serializers
from jobs.views import Jobs


class UserSerializer(serializers.HyperlinkedModelSerializer):
    jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Jobs.objects.all())
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups', 'jobs']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']