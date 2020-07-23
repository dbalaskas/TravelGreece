from datetime import datetime
from django.db import models

from accounts.models import Account

listing_types = [
    ('Studio','Studio'),
    ('Loft','Loft'),
    ('Garden Apartment','Garden Apartment'),
    ('High-rise','High-rise'),
    ('Mid-rise','Mid-rise'),
    ('Low-rise','Low-rise'),
    ('Railroad Apartment','Railroad Apartment'),
    ('House','House'),
    ('Villa','Villa'),
    ('Other','Other'),
]

class Listing(models.Model):
    realtor = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    listing_type = models.CharField(max_length=100, choices=listing_types)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    transport = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
    there_is_livingRoom = models.BooleanField()
    pets_accepted = models.BooleanField()
    smoking_accepted = models.BooleanField()
    events_accepted = models.BooleanField()
    garage = models.IntegerField(default=0)
    sqft = models.IntegerField()
    minimum_days_renting = models.IntegerField()
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

rating_range = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class ListingRating(models.Model):
    rating = models.CharField(choices=rating_range, max_length=1)
    comment = models.TextField(blank=True)
    listing = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(Account, on_delete=models.DO_NOTHING)
    posted_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.rating

