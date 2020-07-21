from datetime import datetime
from django.db import models

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
    ('Other','Other')
]


# Create your models here.
class Listing(models.Model):
    # realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    # listing_type = models.CharField(max_length=100, choices=listing_types)
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


# listing_url	scrape_id	last_scraped	name	summary	space	description	experiences_offered	neighborhood_overview	notes	transit	thumbnail_url	medium_url	picture_url	xl_picture_url	host_id	host_url	host_name	host_since	host_location	host_about	host_response_time	host_response_rate	host_acceptance_rate	host_is_superhost	host_thumbnail_url	host_picture_url	host_neighbourhood	host_listings_count	host_total_listings_count	host_verifications	host_has_profile_pic	host_identity_verified	street	neighbourhood	neighbourhood_cleansed	neighbourhood_group_cleansed	city	state	zipcode	market	country_code	country	latitude	longitude	is_location_exact	property_type	room_type	accommodates	bathrooms	bedrooms	beds	bed_type	amenities	square_feet	price	weekly_price	monthly_price	security_deposit	cleaning_fee	guests_included	extra_people	minimum_nights	maximum_nights	calendar_updated	has_availability	availability_30	availability_60	availability_90	availability_365	calendar_last_scraped	number_of_reviews	first_review	last_review	review_scores_rating	review_scores_accuracy	review_scores_cleanliness	review_scores_checkin	review_scores_communication	review_scores_location	review_scores_value	requires_license	license	jurisdiction_names	instant_bookable	cancellation_policy	require_guest_profile_picture	require_guest_phone_verification	calculated_host_listings_count	reviews_per_month
