from rest_framework import serializers
from slots.models import Slot
from experiences.models import Experience
from bookings.models import Booking

class SimpleExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = ["id", "title", "location", "price"]

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

    def validate(self, data):
        print(data["slot"].id)
        slot = Slot.objects.filter(id=data["slot"].id).first()

        if slot.availableSeats < data['person']:
            raise serializers.ValidationError(f"{data['person']} seats are not available.")
        return data