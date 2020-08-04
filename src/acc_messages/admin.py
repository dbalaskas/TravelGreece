from django.contrib import admin
from acc_messages.models import Message 
# Register your models here.




class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'listing' ,'title', 'mtext', 'date')
    list_display_links = ('id', 'sender', 'receiver', 'listing')
    search_fields = ('listing__title',)
    list_filter = ('sender', 'receiver', 'listing')
    list_per_page = 25

admin.site.register(Message, MessageAdmin)
