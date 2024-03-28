from django.test import TestCase
from car_management.models import Division
from car_management.forms import DivisionForm


#model test
class DivisionTest(TestCase):
    def create_division(self, code="mahmakah konstitusi", division="bangsat"):
        return division.objects.create(code=code, division=division)
        
