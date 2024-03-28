from django.forms import ModelForm, TextInput,SelectMultiple,Select
from django import forms
from .models import *

class FrozenForm(ModelForm):

    incoming_date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'type': 'date',
        })
    )

    name = forms.CharField(widget=forms.Select)
    class Meta:
        model = Frozen
        fields = '__all__'

    # do_number, code, name, quantity, package, incoming_date, processed, unprocessed, pic, supplier, created_at, updated_at

class UnitForm(ModelForm):
    class Meta:
        model = Unit
        fields = '__all__'

class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'

class PicForm(ModelForm):
    class Meta:
        model = Pic
        fields = '__all__'

class SupplierForm(ModelForm):
    class Meta:
        model = Supplier
        fields = '__all__'
