from django.contrib import admin

from .models import Bunch

class BunchAdmin(admin.ModelAdmin):
    list_display=['count','outside','shape','color','sugar','stage']

# Register your models here.
admin.site.register(Bunch,BunchAdmin)