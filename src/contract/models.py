from django.db import models
from datetime import datetime
from accounts.models import Account
from listings.models import Listing


class Contract(models.Model):
	customer=models.ForeignKey(Account, related_name='customer', on_delete=models.DO_NOTHING)
	host=models.ForeignKey(Account, related_name='host' ,on_delete=models.DO_NOTHING)
	listing=models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
	addedinfo=models.CharField(max_length=200)
	entrance_date=models.DateTimeField(blank=True)
	exit_date=models.DateTimeField(blank=True)
	deal_date=models.DateTimeField(default=datetime.now, blank=True)
	price=models.FloatField()


