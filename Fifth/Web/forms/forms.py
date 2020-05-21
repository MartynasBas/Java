from django import forms
from . import models


class GoodsForm(forms.ModelForm):
    class Meta:
        model = models.Good
        fields = ("name", "unit", "amount", "cost", "purpose")


class GeneralForm(forms.ModelForm):
    class Meta:
        model = models.Form
        fields = ("company_title", "order_no", "location", "seller_company_title", "serial_id", "serial_no", "commissioners")
