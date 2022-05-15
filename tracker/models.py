from pyexpat import model
from statistics import mode
from django.db import models
from django.conf import settings
from django.utils import timezone


class TrackRecord(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_and_time = models.DateTimeField(default= timezone.now)
    payment_type = models.CharField(max_length=25)
    transaction_type = models.CharField(max_length=25) 
    category = models.CharField(max_length=25)  
    amount = models.IntegerField() 
    note = models.TextField()