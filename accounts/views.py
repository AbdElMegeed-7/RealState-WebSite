from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if password match
        if password == password2:
            
            # Check UserName
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That UserName is Taken')
                return redirect('register')
            else:
                
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That Email is Taken')
                    return redirect('register')
                else:
                    # Looks Good
                    user = User.objects.user = User.objects.create_user(
                        first_name=first_name,
                        last_name=last_name,
                        username=username,
                        email=email,
                        password=password,
                        password2=password2,
                    )
                    # Login After Register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now Loggid in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')
                    return redirect('login')
        
        else:
            messages.error(request, 'PassWord Does Not Match')
            return redirect('register')
    
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == "POST":
        #
        return
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    return redirect('index')


def dashboard(request):
    return render(request, 'accounts/dashboard.html')