from django.db import models
from cloudinary.models import CloudinaryField
from datetime import datetime

# Create your models here.


class Invoice(models.Model):
    # Description of the expenses
    invoice = models.CharField(
        max_length=50,
        blank=False
    )
    # Description of the expenses
    invoice_reference = models.CharField(
        max_length=50,
        blank=True,
        default=None
    )
    # Tag to a carplate else set to admin
    car_plate = models.CharField(
        max_length=8,
        blank=True,
        default="Admin"
    )
    # Accounts Receivable
    accounts_receivables = models.DecimalField(
        blank=False,
        max_digits=7,
        decimal_places=2,
        default=0
    )
    # Credit/Debit
    BALANCE = [
        ('Credit', 'Credit'),
        ('Debit', 'Debit'),
    ]
    balance = models.CharField(
        max_length=6,
        choices=BALANCE,
        blank=False,
    )
    # Accounts Payable (Supplier Name)
    accounts_payable = models.CharField(
        max_length=50,
        blank=False,
    )
    paid = models.BooleanField(
        default=False
    )
    # Invoice Date
    inv_date = models.DateField()

    # Submitter - value to be assigned
    submitter = models.CharField(
        max_length=50,
        blank=False,
        default="Unknown"
    )
    claim = models.BooleanField(
        default=False
    )
    # Financial_year - value to be assigned
    financial_year = models.IntegerField(
        default=9999
    )
    # Month - value to be assigned=
    month = models.IntegerField(
        default=99
    )

    cover = CloudinaryField(
        default="None"
    )

    log_datetime = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return (self.invoice + " [" + self.car_plate + ']')
