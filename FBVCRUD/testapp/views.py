from django.shortcuts import render,redirect
from .models import Employee
from .forms import EmployeeForm

def list(request):
    form=Employee.objects.all()
    return render (request,'testapp/list.html',{'form':form})

def insert(request):
    form=EmployeeForm()
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('/')
    return render(request,'testapp/insert.html',{'form':form})

def update(request,id):
    employee=Employee.objects.get(id=id)
    form=EmployeeForm(instance=employee)
    if request.method=='POST':
        form=EmployeeForm(request.POST,instance=employee)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request,'testapp/update.html',{'form':form})

def delete(request,id):
    form=Employee.objects.get(id=id)
    form.delete()
    return redirect('/')