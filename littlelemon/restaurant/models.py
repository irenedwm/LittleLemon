from django.db import models

# Create your models here.
class Booking(models.Model):
    BookingID = models.IntegerField()
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    MenuID = models.IntegerField()
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=10)
    Inventory = models.IntegerField()
