from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from experiences.models import Experience
from experiences.serializers import ExperienceSerializer
from rest_framework.response import Response
from slots.models import Slot
from slots.serializers import SlotSerializer

# Create your views here.
class ExperienceViewSet(ModelViewSet):
    # queryset = Experience.objects.all()
    serializer_class = ExperienceSerializer

    def get_queryset(self):
        print(self.request.query_params)
        return Experience.objects.all()

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        slots = SlotSerializer(Slot.objects.filter(experience=serializer.data["id"]), many=True)
        return Response({"experience": serializer.data, "slots": slots.data})