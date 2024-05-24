from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.http import HttpResponse

from .models import Student

def index(request):
    #students = Student.objects.all()
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Email = request.POST['email']
        Password = request.POST['password']
        Password2 = request.POST['password2']
        if Password == Password2:
            if User.objects.filter(email=Email).exists():
                messages.info(request, 'email Already Used')
                return redirect('register')
            elif User.objects.filter(username=Username).exists():
                messages.info(request, 'Username Already Used')
                return redirect('register')
            else:
                user = User.objects.create_user(username=Username,password=Password,email=Email)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Password not the same')
            return redirect('register')
    else:
        return render(request, 'register.html')
    
    
def login(request):
    if request.method == 'POST':
        Username = request.POST['username']
        Password = request.POST['password']
        user = auth.authenticate(username = Username,password=Password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Crediencials not found')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
    

def logout(request):
    auth.logout(request)
    return redirect('root')


def root(request):
    return render(request, 'root.html')
        
   
# Create your views here.

def counting(request):
    text = request.POST['text']
    amount = len(text.split())
    content={
        "text" : text,
        "amount" : amount
    }
    return render(request, 'counting.html', content)
