from django.db import models
import datetime
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

#Unit Class
class Unit(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

#Gender Class
class Gender(models.Model):
    code = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)

    def __str__(self):
        return self.gender

#Position Class
class Position(models.Model):
    code = models.CharField(max_length=10)
    position = models.CharField(max_length=50)

    def __str__(self):
        return self.position

#Impurity Class
class Impurity(models.Model):
    type_impurity = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    quantity = models.IntegerField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Pic Class
class Pic(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Supplier Class
class Supplier(models.Model):
    code = models.CharField(max_length=50)
    name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=100)
    supplier_pic = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#Categories Class
class Categories(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=50)

    def __str__(self):
        return  self.name

#Material Class
class Material(models.Model):
    code = models.CharField(max_length=10)
    name = models.CharField(max_length=100)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    descriptions = models.TextField()

    def __str__(self):
        return self.name


#Frozen Class
class Frozen(models.Model):
    do_number = models.CharField(max_length=30)
    code = models.CharField(max_length=10)
    name = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.ForeignKey(Unit, on_delete=models.CASCADE)
    package = models.IntegerField()
    incoming_date = models.DateField()
    pic = models.ForeignKey(Pic, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(default="WAITING", max_length=20 )

    #do_number, code, name, quantity, package, incoming_date, processed, unprocessed, pic, supplier, created_at, updated_at

    def __str__(self):
        return self.do_number

# processed material
class ProcessedMaterial(models.Model):
    do_number = models.ForeignKey(Frozen, on_delete=models.CASCADE)
    passed = models.IntegerField()
    passed_desc = models.TextField()
    hold = models.IntegerField()
    hold_desc = models.TextField()

    def __str__(self):
        return self.passed
