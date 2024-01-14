from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
global msg_display

def login(request):
    if request.method == 'POST':
        username = request.POST['admn_no']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/home")
        else:
            msg_display = True
            messages.info(request,'*Invalid credentials')
            return render(request,"login.html",{'msg_display':msg_display})
    else:
        return render(request,"login.html")

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        username = request.POST['admn_no']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'*Account already exists')
                return redirect("/register/")
            else:
                user = User.objects.create_user(username=username,password=password1,first_name=first_name)
                user.save();
                return redirect('/')
        else:
            messages.info(request,'*Password not matching')
            return redirect('/register/')

    else:
        return render(request,"register.html")