from rest_framework import serializers
from slots.models import Slot
from experiences.models import Experience
from bookings.models import Booking

class SimpleExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "location"]

class SimpleSlotSerializer(serializers.ModelSerializer):
    experience = SimpleExperienceSerializer()
    class Meta:
        model = Slot
        fields = ["id", "date", "time", "experience"]

class BookingSerializer(serializers.ModelSerializer):
    slot = SimpleSlotSerializer()
    class Meta:
        model = Booking
        fields = ["id", "name", "email", "price", "person", "slot"]

class CreateBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ["id", "name", "email", "price", "person", "slot"]