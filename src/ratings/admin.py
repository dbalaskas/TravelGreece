from django.contrib import admin

from .models import ListingRating

# Register your models here.
class ListingRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'comment')
    list_display_links = ('id', 'rating')
    # list_filter = ('listing_id',)
    # search_fields = ('listing_id',)
    list_per_page = 25

admin.site.register(ListingRating, ListingRatingAdmin)