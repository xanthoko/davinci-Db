from rest_framework import serializers

from hotels.models import Unit, Reservation


class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('country', 'city', 'rating', 'unitId')


class createReservation(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
