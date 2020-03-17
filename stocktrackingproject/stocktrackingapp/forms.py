from django import forms
from .models import StockType, StockPerformance, FinanceResource

class StockTypeForm(forms.ModelForm):
    class Meta:
        model=StockType
        fields='__all__'

class StockPerformanceForm(forms.ModelForm):
    class Meta:
        model=StockPerformance
        fields='__all__'

class FinanceResourceForm(forms.ModelForm):
    class Meta:
        model=FinanceResource
        fields='__all__'