from django.contrib import admin

from .models import Listing, ListingRating

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'neighborhood', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'neighborhood')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'neighborhood')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)

class ListingRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'comment', 'listing', 'user')
    list_display_links = ('id', 'rating', 'comment')
    list_filter = ('rating',)
    search_fields = ('comment', 'listing__title')
    list_per_page = 25

admin.site.register(ListingRating, ListingRatingAdmin)