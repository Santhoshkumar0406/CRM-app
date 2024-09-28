from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import RegisterForm,addrecordForm
from .models import Record

def home(request):
    records = Record.objects.all()

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully')
            return redirect('home_page')
        else:
            messages.error(request, 'There was an error occured')
            return redirect ('home_page')

    return render (request, 'home.html' , {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect ('home_page')

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate (request, username = username, password = password)
            login(request,user)
            messages.success(request,'Wellcome')
            return redirect ('home_page')
    else:
        form = RegisterForm()
        return render (request, 'register.html' , {'form':form})
    return render (request, 'register.html' , {'form':form})

def record(request,pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'records.html',{'customer_record':customer_record})
    
    else:
        messages.error(request,'You must Logged in')
        return redirect ('home_page')
    
def deleterecord (request,pk):
    if request.user.is_authenticated:
        delete = Record.objects.get(id=pk)
        delete.delete()
        messages.success(request,'Successfully Deleted')
        return redirect('home_page')
    else:
        messages.success(request,'You must Logged in')
        return redirect('home_page')
    
def addrecord(request):
    form = addrecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == 'POST':
            if form.is_valid():
                addrecord = form.save()
                messages.success(request,'Successfully created')
                return redirect ('home_page')
        return render(request, 'addrecord.html',{'form':form})
    else:
        messages.error(request,'You must be Logged in')
        return redirect ('home_page')
    
def updaterecord(request,pk):
    if request.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = addrecordForm(request.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,'Successfully updated')
            return redirect ('home_page')
        return render(request,'updaterecord.html',{'form':form})
    else:
        messages.error(request,'You must be Logged in')
        return redirect ('home_page')
            


