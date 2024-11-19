from django.contrib import admin

from .models import Client, Payment

class ClientAdmin(admin.ModelAdmin):
    list_display=['name','balance','credit','manager']

class PaymentAdmin(admin.ModelAdmin):
    list_display=['client','timestamp','purpose','amount',]

admin.site.register(Client,ClientAdmin)
admin.site.register(Payment,PaymentAdmin)