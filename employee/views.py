from django.shortcuts import render, redirect, get_object_or_404
import os.path
import os
from django.conf import settings
from employee.models import record

# Create your views here.

def base(request):
    return render(request, 'employee/base.html', {})

def newemployee(request):
    return render(request, 'employee/newemployee.html')

def displayemployee(request):
    a = record.objects.all()
    return render(request, 'employee/displayemployee.html', {"a":a})

def header(request):
    return render(request, 'employee/header.html', {})

def addemployee(request):
    print(request.POST)
    name = request.POST['name']
    gender = request.POST['gender']
    department = request.POST['department']
    salary = request.POST['salary']
    emp = record(name=name, gender=gender, department=department, salary=salary)
    emp.save()
    return render(request, 'employee/newemployee.html', {})

def deleterecord(request, employee_id):
    a = record.objects.filter(id=employee_id)
    a.delete()
    b = record.objects.all()
    return render(request, 'employee/displayemployee.html', {"a":b})

def editrecord(request, employee_id):
    x = record.objects.filter(id=employee_id)
    return render(request, 'employee/editemployee.html', {"x":x} )

def updateemployee(request):
    print(request.POST)
    obj = record.objects.get(id= request.POST['id'])
    obj.name = request.POST['name']
    obj.gender = request.POST['gender']
    obj.department = request.POST['department']
    obj.salary = request.POST['salary']
    obj.save()
    return redirect('displayemployee')
