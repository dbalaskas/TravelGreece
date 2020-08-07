from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Account, RealtorRating

class AccoutInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = 'employee'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('id', 'username', 'first_name', 'last_name', 'email', 'realtor')
    list_display_links = ('id', 'username', 'first_name', 'last_name')
    # list_filter = ('realtor',)
    # list_editable = ('realtor',)
    search_fields = ('username', 'first_name', 'last_name')
    list_per_page = 25
    inlines = (AccoutInline,)

    def realtor(self, obj):
        return Account.objects.get(user=obj).is_realtor

    realtor.short_description = 'Realtor'

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

class RealtorRatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'rating', 'comment', 'realtor', 'rater')
    list_display_links = ('id', 'rating', 'comment')
    list_filter = ('rating',)
    search_fields = ('comment', 'realtor__user__username', 'realtor_user__first_name', 'realtor__user__last_name')
    list_per_page = 25

admin.site.register(RealtorRating, RealtorRatingAdmin)