from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class StockType(models.Model):
    stockname=models.CharField(max_length=255)
    stockticker=models.CharField(max_length=50)
    stockdescription=models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.stockname
    
    class Meta:
        db_table='stocktype'
        verbose_name_plural='stocktypes'

    
class StockPerformance(models.Model):
    stockHighPrice=models.DecimalField(max_digits=10, decimal_places=2)
    stockLowPrice=models.DecimalField(max_digits=10,decimal_places=2)
    stockBuyPrice=models.DecimalField(max_digits=10,decimal_places=2)
    stockBuyDate=models.DateField()
    user=models.ForeignKey(User, on_delete=models.DO_NOTHING)
    stockticker=models.ForeignKey(StockType, on_delete=models.DO_NOTHING)
    stockAdditionalInfo=models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.stockticker)

    class Meta:
        db_table='stockperformance'
        verbose_name_plural='stockperformances'

class FinanceResource(models.Model):
    resourcename=models.CharField(max_length=255)
    resourcetype=models.CharField(max_length=200)
    user=models.ManyToManyField(User)
    resourcedescription=models.TextField(null=True, blank=True)
    date=models.DateField()

    def __str__(self):
        return self.resourcename

    class Meta:
        db_table='financeresource'
        verbose_name_plural='financeresources'