import requests
from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import Http404
from .forms import *
from django.contrib import messages
from django.shortcuts import redirect,render, get_object_or_404

def indexFrozen(requests):
    data = Frozen.objects.values(
        'code', 'name', 'package','quantity__name','supplier__name', 'pic__name'
    )
    return render(requests,'infrozen/frozen-index.html', {"data" : data})

def editFrozen(request, id):
    frozen = get_object_or_404(Frozen, id=id)

    if request.method == 'GET':
        context = {'form' : UnitForm( instance=frozen ), 'id':id}
        return render(request, 'infrozen/editfrozen.html', context)

    elif request.method == 'POST':
        form = FrozenForm(request.POST, instance=frozen)
        if form.is_valid():
            form.save()
            messages.success(request, "BERHASIL EDIT DATA")
            return redirect('indexunit')
        else:
            messages.error(request, "NGGA BISA")
            return render(request, 'infrozen/unit-index.html', {'form':form})

def indexUnit(request):
    data = Unit.objects.values(
        'code', 'name',
    )
    return render(request, 'infrozen/unit-index.html', {'data': data})

def editUnit(request, id):
    unit = get_object_or_404(Unit, id=id)

    if request.method == 'GET':
        context = {'form' : UnitForm( instance=unit ), 'id':id}
        return render(request, 'infrozen/editunit.html', context)

    elif request.method == 'POST':
        form = UnitForm(request.POST, instance=unit)
        if form.is_valid():
            form.save()
            messages.success(request, "BERHASIL EDIT DATA")
            return redirect('indexunit')
        else:
            messages.error(request, "NGGA BISA")
            return render(request, 'infrozen/unit-index.html', {'form':form})

def deleteUnit(request, id):
    unit = Unit.objects.get( id = id)
    unit.delete()
    return redirect('indexunit')


def addfrozen(request):
    form = FrozenForm
    template = 'infrozen/addfrozen.html'
    if request.method == 'POST':
        form = FrozenForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Success add data")
            return redirect('index')
    context = {'form':form}
    return render(request, template, context)


def addUnit(requests):
    form = UnitForm
    template = 'infrozen/addfrozen.html'
    if requests.method == 'POST':
        form = UnitForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.success(requests, "add unit successfully")
            return redirect('addunit')
    context = {'form':form}
    return render(requests, template,context)

def addPic(requests):
    form = PicForm
    template = 'infrozen/addfrozen.html'
    if requests.method == 'POST':
        form = PicForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.succes(requests, "add PIC successfully")
            return redirect('')
    context = {'form':form}
    return render(requests, template,context)

def addSupplier(requests):
    form = SupplierForm
    template = 'infrozen/addfrozen.html'
    if requests.method == 'POST':
        form = SupplierForm(requests.POST)
        if form.is_valid():
            form.save()
            messages.success(requests, "add supplier succesfully")
    context = {'form': form}
    return render(requests, template, context)