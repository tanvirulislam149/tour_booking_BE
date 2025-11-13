from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from experiences.models import Experience
from experiences.serializers import ExperienceSerializer

# Create your views here.
class ExperienceViewSet(ModelViewSet):
    queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer