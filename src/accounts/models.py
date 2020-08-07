from django.contrib.auth.models import User
from django.db import models
from datetime import datetime

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_realtor = models.BooleanField(default=False)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    description = models.TextField(blank=True)

# class Account(models.Model):
#     userName = models.CharField(max_length=50)
#     firstName = models.CharField(max_length=30)
#     lastName = models.CharField(max_length=30)
#     email = models.CharField(max_length=50)
#     phone = models.CharField(max_length=20, blank=True)
#     description = models.TextField(blank=True)
#     registered_date = models.DateField(default=datetime.now, blank=True)
#     is_realtor = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

rating_range = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class RealtorRating(models.Model):
    rating = models.CharField(choices=rating_range, max_length=1)
    comment = models.TextField(blank=True)
    realtor = models.ForeignKey(Account, related_name='realtor', on_delete=models.DO_NOTHING)
    rater = models.ForeignKey(Account, related_name='rater', on_delete=models.DO_NOTHING)
    posted_date = models.DateField(default=datetime.now, blank=True)

    def __str__(self):
        return self.rating