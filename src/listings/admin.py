from django.contrib import admin

from .models import Listing

# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'city', 'neighborhood', 'list_date')
    list_display_links = ('id', 'title')
    list_filter = ('city', 'neighborhood')
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'neighborhood')
    list_per_page = 25

admin.site.register(Listing, ListingAdmin)