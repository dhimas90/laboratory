from django.urls import path
from . import views

urlpatterns = [
    path("frozen-index/", views.indexFrozen, name='indexfrozen'),
    path("add-frozen/", views.addfrozen, name='addfrozen'),
    path("frozen-edit/<int:id>", views.editFrozen, name='editfrozen'),

    path("unit-index/", views.indexUnit, name='indexunit'),
    path("add-unit/", views.addUnit, name='addunit'),
    path("unit-edit/<int:id>", views.editUnit, name='editunit'),
    path("unit-delete/<int:id>", views.deleteUnit, name='deleteunit'),

    path("add-pic/", views.addPic, name='addpic'),
    path("add-supplier/", views.addSupplier, name='addsupplier'),
]
