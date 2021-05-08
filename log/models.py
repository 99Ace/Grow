from django.db import models
from datetime import datetime

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

    log_datetime = models.DateTimeField(
        default=datetime.now
    )

    def __str__(self):
        return (
            self.invoice +
            " (" +
            str(self.log_datetime) +
            '), action='
            + self.action)
