from rest_framework import generics, permissions
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse


def home(request):
    return HttpResponse("Welcome to CrwondFundMe API")

# List all projects


class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

# Retrieve, update, delete a project


class ProjectDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated]

# Create a pledge


class PledgeCreateView(generics.CreateAPIView):
    serializer_class = PledgeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(backer=self.request.user)
