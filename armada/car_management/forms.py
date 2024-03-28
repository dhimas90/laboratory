from django.forms import ModelForm
from django import forms
from .models import Car, Person_in_charge, Driver, Category, Transmission, Position, Trip, Brand, Division, Maintenance, List_Maintenance, Gender
# from django.contrib.auth.models import User

# class UserForm(forms.ModelForm):
#     class Meta:
#         model= User
#         field = ['username', 'password']

# class UserRegistration(forms.ModelForm):
#     class Meta:
#         fields = [
#             'username', 
#             'password',
#             'email',
#             'first_name',
#             'last_name',
#         ]

class CarForm(ModelForm):
    legal_number = forms.CharField(max_length=200, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    image_vehicle_number = forms.ImageField(max_length=255)
    police_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    release_year = forms.DateField(
        
        widget=forms.DateInput(attrs={"type": "date", "autocomplete": "off"}),
    )
    color = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    series = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    total_distance = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    price = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    car_type = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"autocomplete":"off"}))
    car_image = forms.ImageField(max_length=255)
    transmission = forms.ModelChoiceField(queryset=Transmission.objects.all())
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    class Meta:
        model = Car
        fields = '__all__'

class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class TransmissionForm(ModelForm):
    class Meta:
        model = Transmission
        fields = '__all__'

class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'

class TripForm(ModelForm):
    class Meta:
        model = Trip
        fields = '__all__'

class DivisionForm(ModelForm):
    class Meta:
        model = Division
        fields = '__all__'

class DriverForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'autocomplete' : 'off'}))
    birth = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date', 'autocomplete':'off'})
    )
    class Meta:
        model = Driver
        fields = '__all__'

class PersoninChargeForms(ModelForm):
    birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'autocomplete': 'off'})
    )
    # gender = forms.ModelChoiceField(queryset=Gender.objects.all())
    # position = forms.ModelChoiceField(queryset=Position.objects.all())
    # division = forms.ModelChoiceField(queryset=Division.objects.all())
    class Meta:
        model = Person_in_charge
        fields = "__all__"
        #     [
        #     'name',
        #     'birth',
        #     'identity_number',
        #     'image_identity_number',
        #     'division',
        #     'gender',
        #     'position',
        # ]

class BrandForm(ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'

class GenderForm(ModelForm):
    class Meta:
        model = Gender
        fields = '__all__'

class MaintenanceForm(ModelForm):
    class Meta:
        model = Maintenance
        fields = '__all__'