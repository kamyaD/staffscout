from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password
from .models import User
from jobs.models import Jobs

class UserSerializer(serializers.ModelSerializer):
    # jobs = serializers.PrimaryKeyRelatedField(many=True, queryset=Jobs.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'bio', 'profile_pic', 'city', 'country', 'job_title','availability_status')
        read_only_field = ('username',)

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username',  'email', 'password', 'password2','first_name', 'last_name', 'bio', 'profile_pic', 'city', 'country', 'job_title', 'availability_status','is_employer','is_candidate','is_both_employer_and_candidate')

        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        
        }

    def validate(self, attrs):
        if attrs['password'] !=attrs['password2']:
            raise serializers.ValidationError({"password": "password fields didn't match."})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email =  validated_data['email'],
            password =  validated_data['password'],
            password2 =  validated_data['password2'],
            first_name =  validated_data['first_name'],
            last_name =  validated_data['last_name'],
            bio =  validated_data['bio'],
            profile_pic =  validated_data['profile_pic'],
            city =  validated_data['city'],
            country =  validated_data['country'],
            job_title =  validated_data['job_title'],
            availability_status =  validated_data['availability_status'],
            is_employer =  validated_data['is_employer'],
            is_candidate =  validated_data['is_candidate'],
            is_both_employer_and_candidate =  validated_data['is_both_employer_and_candidate']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

