from rest_framework import serializers
from slots.models import Slot
from experiences.serializers import ExperienceSerializer

class SlotSerializer(serializers.ModelSerializer):
    experience = ExperienceSerializer()
    class Meta:
        model = Slot
        fields = ["id", "date", "time", "availableSeats", "total_seats", "experience"]