from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User
from jobs.models import Jobs
from candidate.models import Profiles
from django.contrib.auth import authenticate
from rest_framework import serializers
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.utils.translation import gettext as _
from rest_framework.authtoken.models import Token



class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name','email', 'is_employer', 'is_candidate','is_both_employer_and_candidate']
        # read_only_field = ('username',)



class ProfilesSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profiles
        fields = [
            'id','user','specialism_id','experiences_id','profile_pic', 'city', 'country', 'job_title','availability_status','education_levels_id','job_title','personal_statement','personal','biography','education','experience','portfolio','skills','honors','availability_status','metadata','created_at','updated_at','deleted_at']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create_user(**user_data)
        user.set_password(self.context.get('request').data['user']['password'])
        user.save()
        validated_data['user'] = user
        
        profile = Profiles.objects.create(**validated_data)
        return profile



class ProfilesUpdateSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Profiles
        fields = ProfilesSerializer.Meta.fields

class UserLoginSerializer(AuthTokenSerializer):
    username = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs




