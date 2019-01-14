from django.contrib import admin
from hotels.models import Unit, Building, Room, Reservation, Customer, Reservation_Payment


# Register your models here.
admin.site.register(Unit)
admin.site.register(Building)
admin.site.register(Room)
admin.site.register(Reservation)
admin.site.register(Customer)
admin.site.register(Reservation_Payment)