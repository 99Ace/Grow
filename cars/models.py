from django.db import models

# Create your models here.


class CarDeal(models.Model):
    deal_ref = models.CharField(
        max_length=10,
        blank=False
    )
    car_plate = models.CharField(
        max_length=8,
        blank=False
    )
    chassis_no = models.CharField(
        max_length=25,
        blank=True,
        default="none"
    )
    engine_no = models.CharField(
        max_length=20,
        blank=True,
        default="none"
    )
    current_owner = models.CharField(
        max_length=30,
        blank=True,
        default="none"
    )
    buyer = models.CharField(
        max_length=30,
        blank=True,
        default="none"
    )
    seller = models.CharField(
        max_length=30,
        blank=True,
        default="none"
    )
    referral = models.CharField(
        max_length=30,
        blank=True,
        default="none"
    )

    def __str__(self):
        return (self.deal_ref+" ("+self.car_plate+")")
