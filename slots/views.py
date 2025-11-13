from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from slots.models import Slot
from slots.serializers import SlotSerializer

# Create your views here.
class SlotViewSet(ModelViewSet):
    queryset = Slot.objects.all()
    serializer_class = SlotSerializer