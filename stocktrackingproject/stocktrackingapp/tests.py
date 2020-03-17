from django.test import TestCase
from .models import StockType, StockPerformance, FinanceResource

# Create your tests here.
def test_string(self):
    type=StockType(typename='Spotify')
    self.assetEqual(str(type), type.stockname)

def test_table(self):
    self.assertEqual(str(StockType._meta.db_table), 'stocktype')

class StockTypeTest(TestCase):
    def setup(self):
        stockname=StockType(stockname='Spotify')
    
    def test_string(self):
        stock=self.setup()
        self.assertEqual(str(stock), stock.stockname)

class FinanceResourceTest(TestCase):
    def test_string(self):
        resource=FinanceResource(resourcename="Valor")
        self.assertEqual(str(resource), resource.resourcename)

    def test_table(self):
        self.assertEqual(str(FinanceResource._meta.db_table), 'resource')