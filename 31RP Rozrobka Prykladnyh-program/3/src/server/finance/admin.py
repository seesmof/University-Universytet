from django.contrib import admin

from .models import Client, Payment, PeriodicPayment

class ClientAdmin(admin.ModelAdmin):
    list_display=['name','balance','credit','manager']

class PaymentAdmin(admin.ModelAdmin):
    list_display=['client','amount','purpose','operation','kind','timestamp',]

class PeriodicPaymentAdmin(admin.ModelAdmin):
    list_display=['client','amount','purpose','period','next_date',]

admin.site.register(Client,ClientAdmin)
admin.site.register(Payment,PaymentAdmin)
admin.site.register(PeriodicPayment,PeriodicPaymentAdmin)