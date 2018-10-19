from django.forms import ModelForm
from .models import Widget


class FillForm(ModelForm):
    class Meta:
        model = Widget
        fields = ['description', 'quantity']
