from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from bookings.models import Booking
from slots.models import Slot
from bookings.serializers import BookingSerializer, CreateBookingSerializer

# Create your views here.
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    
    def get_serializer_class(self):
        if self.request.method in ["POST", "PUT", "PATCH"]:
            return CreateBookingSerializer
        else:
            return BookingSerializer
        
    def perform_create(self, serializer):
        serializer.save()
        slot_id = serializer.data["slot"]
        slot = Slot.objects.filter(id = slot_id).first()
        slot.availableSeats -= serializer.data["person"]
        slot.save()