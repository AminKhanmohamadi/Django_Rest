from django.contrib import admin

from config.apps.inventory.models import StockRecord

# Register your models here.
admin.site.register(StockRecord)