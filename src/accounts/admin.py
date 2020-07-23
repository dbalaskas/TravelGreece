from django.contrib import admin

from .models import Account, RealtorRating


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'userName', 'firstName', 'lastName', 'email', 'is_realtor', 'registered_date')
    list_display_links = ('id', 'userName', 'firstName', 'lastName')
    list_filter = ('is_realtor',)
    list_editable = ('is_realtor',)
    search_fields = ('userName', 'firstName', 'lastName')
    list_per_page = 25

admin.site.register(Account, AccountAdmin)

class RealtorRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'comment', 'realtor', 'user')
    list_display_links = ('id', 'rating', 'comment')
    list_filter = ('rating',)
    search_fields = ('comment', 'realtor__userName', 'realtor_firstName', 'realtor__lastName')
    list_per_page = 25

admin.site.register(RealtorRating, RealtorRatingAdmin)