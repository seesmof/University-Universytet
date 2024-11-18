from django.contrib import admin

from .models import User, Transaction

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'balance', 'credit_limit')

# Register your models here.
admin.site.register(User, UserAdmin)
admin.site.register(Transaction)