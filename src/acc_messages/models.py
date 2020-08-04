from django.db import models
from datetime import datetime
from accounts.models import Account
from listings.models import Listing



class Message(models.Model):
	sender=models.ForeignKey(Account, related_name='sender', on_delete=models.DO_NOTHING)
	receiver=models.ForeignKey(Account, related_name='receiver' ,on_delete=models.DO_NOTHING)
	listing=models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
	title=models.CharField(max_length=100)
	mtext=models.CharField(max_length=200)
	read=models.BooleanField(default=False)
	date=models.DateTimeField(default=datetime.now, blank=True)
