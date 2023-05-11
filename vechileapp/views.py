from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Vehicle
from . forms import VehicleForm

# Create your views here.
def index(request):
    obj=Vehicle.objects.all()
    return render(request,'index.html', {'result':obj})
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('adminview')
        else:
            messages.info(request,'Invalid person')
            return redirect('login')



    return render(request,'login.html')
def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        conpass=request.POST['conpass']
        if password == conpass:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password,email=email)
                user.save()
                print('saved')
                return redirect('login')
        else:
            messages.info(request, 'Password not matching')
            return redirect('signup')
        return redirect('/')

    return render(request,'signup.html')

def update(request,id):
    task=Vehicle.objects.get(id=id)
    formdata=VehicleForm(request.POST or None, request.FILES, instance=task)
    if formdata.is_valid():
        formdata.save()
        return redirect('adminview')
    return render(request,'update.html',{'form':formdata,'task':task})

def details(request, task_id):
    detail = Vehicle.objects.get(id=task_id)

    return render(request,'details.html', {'detail': detail})

def logout(request):
    auth.logout(request)
    return redirect('/')

def adminview(request):
    obj = Vehicle.objects.all()
    return render(request, 'adminview.html', {'result': obj})
def admindetail(request, admintask_id):
    detail = Vehicle.objects.get(id=admintask_id)

    return render(request,'admindetail.html', {'detail': detail})