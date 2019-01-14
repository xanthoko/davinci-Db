from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view

from hotels.models import Reservation_Has_Room, Reservation, Reservation_Payment
from hotels.models import Unit, Room
from hotels.serializers import listSerializer, createReservation


class listHotels(generics.ListAPIView):
    queryset = Unit.objects.all()
    serializer_class = listSerializer


class createReservationView(generics.ListCreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = createReservation

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # save survey to the user
        res = serializer.save()
        headers = self.get_success_headers(serializer.data)

        fromDate = request.data.get('dateFrom')
        toDate = request.data.get('dateTo')
        roomId = request.data.get('roomId', -1)
        try:
            room = Room.objects.get(number=roomId)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        Reservation_Has_Room.objects.create(
            reservationId=res, number=room, fromDate=fromDate, toDate=toDate)

        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers)


@api_view(['POST'])
def book(request):
    rid = Reservation.objects.count()
    Reservation.objects.create(reservationId=rid)
    return Response()


@api_view(['POST'])
def check_room(request):
    people = request.POST.get('people', 1)
    fromDate = request.POST.get('dateFrom', None)
    toDate = request.POST.get('dateTo', None)

    pack1 = Reservation_Has_Room.objects.filter(
        number__beds__gte=people, toDate__lte=fromDate)
    pack2 = Reservation_Has_Room.objects.filter(
        number__beds__gte=people, toDate__gte=toDate)

    available = pack1 | pack2

    if available:
        return Response(available.values_list('number'))
    else:
        return Response()


@api_view(['POST'])
def check_payment(request):
    res_id = request.POST.get('reservationId', None)

    try:
        reserv = Reservation.objects.get(reservationId=res_id)
    except Reservation.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if Reservation_Payment.objects.filter(reservationId=reserv).exists():
        return Response({'payed': True})
    else:
        return Response({'payed': False})
