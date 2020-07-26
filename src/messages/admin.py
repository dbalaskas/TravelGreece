from django.contrib import admin
from messages.models import Message 
# Register your models here.




class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'sender', 'receiver', 'listing' ,'title', 'mtext', 'date', 'read')
    list_display_links = ('id', 'sender', 'receiver', 'listing')
    #search_fields = ('userName', 'firstName', 'lastName')
    list_per_page = 25

admin.site.register(Message, MessageAdmin)
