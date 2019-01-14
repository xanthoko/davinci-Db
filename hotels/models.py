from django.db import models


class Unit(models.Model):
    unitId = models.PositiveSmallIntegerField(primary_key=True)
    rating = models.CharField(max_length=10, null=True, blank=True)
    country = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=50)
    number = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.unitId
        


class Building(models.Model):
    buildingName = models.CharField(max_length=100, primary_key=True)
    unitId = models.ForeignKey(Unit, on_delete=models.CASCADE)
    floors = models.PositiveSmallIntegerField(default=1)
    type = models.CharField(max_length=100, default='main')
    size = models.PositiveSmallIntegerField()

    def __str__(self):
        return self.buildingName


class Room(models.Model):
    number = models.CharField(max_length=7, primary_key=True)
    buildingName = models.ForeignKey(Building, on_delete=models.CASCADE)
    floor = models.PositiveSmallIntegerField()
    beds = models.PositiveSmallIntegerField(default=1)
    view = models.CharField(max_length=20)
    hasBalcony = models.BooleanField()
    isClean = models.BooleanField()

    def __str__(self):
        return '{}: {}'.format(self.number, self.buildingName)


class Customer(models.Model):
    customerId = models.AutoField(primary_key=True)
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(null=True, blank=True)

    @property
    def full_name(self):
        return '{} {}'.format(self.firstName, self.lastName)

    def __str__(self):
        return self.full_name


class Reservation(models.Model):
    reservationId = models.AutoField(primary_key=True)
    customerId = models.ForeignKey(Customer, on_delete=models.CASCADE)
    price = models.PositiveSmallIntegerField()
    numberOfPeople = models.PositiveSmallIntegerField(default=1)


class Reservation_Has_Room(models.Model):
    reservationId = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    number = models.ForeignKey(Room, on_delete=models.CASCADE)
    fromDate = models.DateField()
    toDate = models.DateField()

    @property
    def capacity(self):
        return self.number.numberOfPeople

    def __str__(self):
        return '{} -> {}'.format(self.reservationId, self.number)


class Reservation_Payment(models.Model):
    paymentId = models.AutoField(primary_key=True)
    reservationId = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    isCash = models.BooleanField()
    date = models.DateField()
    creditCard = models.CharField(max_length=30, null=True, blank=True)
