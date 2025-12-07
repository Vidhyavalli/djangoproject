from django.shortcuts import HttpResponse,render,redirect
from .models import data

# Create your views here.

def home(request):
    mydata=data.objects.all()
    return render(request,'index.html',{'Data':mydata})
def addData(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        city=request.POST['city']
        address=request.POST['address']

        obj=data()
        obj.name=name   
        obj.age=age
        obj.city=city
        obj.address=address
        obj.save()
        mydata=data.objects.all()
        
    return render(request,'index.html',{'Data':mydata})
def updateData(request,id):
    mydata=data.objects.get(id=id)
    if request.method=='POST':
        name=request.POST['name']
        age=request.POST['age']
        city=request.POST['city']
        address=request.POST['address']
        mydata.name=name
        mydata.age=age
        mydata.city=city
        mydata.address=address
        mydata.save()
        mydata=data.objects.all()
        return redirect('/')
        
    return render(request,'update.html',{'data':mydata})
def deleteData(request,id):
    mydata=data.objects.get(id=id)
    mydata.delete()
    return redirect('/')