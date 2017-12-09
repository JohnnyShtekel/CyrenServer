from __future__ import unicode_literals
from django.db import models

WORK_CHOICES = (
    ("on vacation","OnVacation"),
    ("working","Working"),
    ("on business trip","Trip"),
)

class User(models.Model):
    status = models.CharField(max_length=20, choices=WORK_CHOICES, default='working')
    userName = models.CharField(max_length=100)
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)

    def __unicode__(self):
        return 'Employee: ' + self.firstName + ' ' + self.lastName + ' status: ' + self.status
