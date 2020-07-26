from django.contrib import admin
from contract.models import Contract 
# Register your models here.




class ContractAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'host', 'listing' ,'entrance_date', 'addedinfo' ,'exit_date', 'deal_date', 'price')
    list_display_links = ('id', 'customer', 'host', 'listing')
    #search_fields = ('userName', 'firstName', 'lastName')
    list_per_page = 25

admin.site.register(Contract, ContractAdmin)
# Register your models here.
