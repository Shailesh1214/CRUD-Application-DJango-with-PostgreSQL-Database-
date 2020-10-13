from django import forms
from django.shortcuts import render
from webapp_pgadmin.models import EmpModel
from django.contrib import messages
from webapp_pgadmin.forms import Empforms
def showemp(request):
    showall=EmpModel.objects.all()
    return render(request,'index.html',{"data":showall})

def Insertemp(request):
    if request.method =="POST":
        if request.POST.get('empname') and request.POST.get('email') and request.POST.get('occuapation') and request.POST.get('salary') and request.POST.get('gender'):
            saverecord=EmpModel()
            saverecord.empname=request.POST.get('empname')
            saverecord.email=request.POST.get('email')
            saverecord.occuapation=request.POST.get('occuapation')
            saverecord.salary=request.POST.get('salary')
            saverecord.gender=request.POST.get('gender')
            saverecord.save()
            messages.success(request,'Employee' +saverecord.empname+ ' Is saved sucessfully.....!')
        return render(request,'insert.html')
    else:
        return render(request,'insert.html')

def Editemp(request,id):
    Editempobj=EmpModel.objects.get(id=id)
    return render(request,'Edit.html',{"EmpModel":Editempobj})
    
def updateemp(request,id):
    Updateemp=EmpModel.objects.get(id=id)
    form=Empforms(request.POST,instance=Updateemp)
    if form.is_valid():
        form.save()
        messages.success(request,'Record Update Successfully....!')
        return render(request,'Edit.html',{"EmpModel":Updateemp})