from django.db import models
# from django.contrib.auth.models import User

class Division(models.Model):
    code = models.CharField(max_length=10)
    division = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.division

class Position(models.Model):
    code = models.CharField(max_length=10)
    position = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.position

class Gender(models.Model):
    GENDER = [
        ("Male","Male"),
        ("Female", "Female"),
        ("N", "Not Set"),
    ]
    gender = models.CharField(max_length=20, choices=GENDER)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.gender

class Person_in_charge(models.Model):
    name = models.CharField(max_length=100)
    position = models.ForeignKey(Position, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    birth = models.DateTimeField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    identity_number = models.CharField(max_length=100)
    image_identity_number = models.ImageField(upload_to='person_in_charge/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name

class Driver(models.Model):
    name = models.CharField(max_length=100)
    driving_lisence_number = models.CharField(max_length=100, unique=True)
    image_driving_lisence = models.ImageField(upload_to='driver/')
    birth = models.DateTimeField()
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    identity_number = models.CharField(max_length=50, unique=True)
    image_identity_number = models.ImageField(upload_to='driver/')
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name
    def delete(self, *args, **kwargs):
        self.image_driving_lisence.delete()
        self.image_identity_number.delete()
        super().delete(*args, **kwargs)

class Transmission(models.Model):
    transmission = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.transmission

class Category(models.Model):

    category = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.category

class Brand(models.Model):
    brand = models.CharField(max_length=50, unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.brand

class Car(models.Model):
    legal_number = models.CharField(max_length=50)
    image_vehicle_number = models.ImageField(upload_to="images/")
    police_number = models.CharField(max_length=50)
    release_year = models.DateTimeField()
    color = models.CharField(max_length=50)
    series = models.CharField(max_length=50)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    total_distance = models.IntegerField()
    price = models.IntegerField()
    car_type = models.CharField(max_length=50)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    car_image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.police_number

    def delete(self, *args, **kwargs):
        self.car_image.delete()
        self.image_vehicle_number.delete()
        super().delete(*args, **kwargs)


class Trip(models.Model):
    letter_number = models.CharField(max_length=50)
    driver_id = models.ForeignKey(Driver, on_delete=models.CASCADE)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    distance_start = models.IntegerField()
    distance_finish = models.IntegerField()
    fuel_receipt = models.ImageField(upload_to='fuel/')
    person_in_charge = models.ForeignKey(Person_in_charge, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.letter_number

class List_Maintenance(models.Model):
    name_part = models.CharField(max_length=50)
    quantity = models.IntegerField()
    distance = models.IntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.name_part

class Maintenance(models.Model):
    letter_number = models.CharField(max_length=50)
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)
    person_in_charge = models.ForeignKey(Person_in_charge, on_delete=models.CASCADE)
    date_of_maintenance = models.DateTimeField()
    image_receipt = models.ImageField(upload_to='maintenance/')
    list = models.ForeignKey(List_Maintenance,null=True, on_delete=models.CASCADE)
    total_amount = models.IntegerField()
    receipt_image = models.FileField(null=True)
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    def __str__(self):
        return self.letter_number
