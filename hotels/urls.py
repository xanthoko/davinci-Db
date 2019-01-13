from django.urls import path

from hotels import views

urlpatterns = [
    path('checkRoom', views.check_room, name='check'),
    path('payed', views.check_room, name='check'),
    path('hotels', views.listHotels.as_view(), name='hotels'),
    path('book', views.createReservationView.as_view(), name='book')
]
