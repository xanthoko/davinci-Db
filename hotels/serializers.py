from rest_framework import serializers

from hotels.models import Unit, Reservation


class listSerializer(serializers.ModelSerializer):
    buildings = serializers.SerializerMethodField()

    class Meta:
        model = Unit
        fields = '__all__'

    def get_buildings(self, obj):
        d = {}
        rs = []
        for r in obj.building_set.all():
            rs.append(r.room_set.values_list('number')) 
            d[r.buildingName] = rs
        return d



class createReservation(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = '__all__'
