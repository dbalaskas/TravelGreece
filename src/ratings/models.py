from django.db import models

rating_range = [
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

# Create your models here.
class ListingRating(models.Model):
    rating = models.CharField(choices=rating_range, max_length=1)
    comment = models.TextField(blank=True)
    # listing_id = models.ForeignKey(Listing, on_delete=models.DO_NOTHING)
    # user_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.rating