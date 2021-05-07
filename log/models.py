from django.db import models
from mikar9.models import Invoice
# Create your models here.


class LogRecord(models.Model):
    invoice = models.CharField(
        max_length=50,
        blank=False
    )

    action = models.CharField(
        max_length=10,
        blank=False
    )
    changes = models.CharField(
        max_length=500,
        blank=False
    )

    submitter = models.CharField(
        max_length=50,
        blank=False,
        default="Unknown"
    )

    """ AUTO ADD THE CREATION DATE """
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.invoice + " [ log @" + str(self.date) + 'action = '+ self.action +']')
