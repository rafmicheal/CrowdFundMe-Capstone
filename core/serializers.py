from rest_framework import serializers
from .models import Project, Pledge
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class ProjectSerializer(serializers.ModelSerializer):
    creator = UserSerializer(read_only=True)

    class Meta:
        model = Project
        fields = '__all__'


class PledgeSerializer(serializers.ModelSerializer):
    backer = UserSerializer(read_only=True)

    class Meta:
        model = Pledge
        fields = '__all__'
