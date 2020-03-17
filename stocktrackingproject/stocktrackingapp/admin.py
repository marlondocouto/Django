from django.contrib import admin
from .models import StockType, StockPerformance, FinanceResource

# Register your models here.
admin.site.register(StockType)
admin.site.register(StockPerformance)
admin.site.register(FinanceResource)