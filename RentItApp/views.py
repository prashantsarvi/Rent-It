from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.utils.safestring import mark_safe

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    return render(request, 'login.html')

def forgotpassword(request):

    if(request.method=='POST'):
        email = request.POST['mail']
        if(User.objects.filter(email = email).exists()):
            password = request.POST['psw']
            repeatpass= request.POST['psw-repeat']
            if(password!=repeatpass):
                messages.info(request, 'Password did not match')
                return render(request, 'forgotpass.html')
            else:
                user = User.objects.filter(email = email)
                user.update(password = password)
                messages.info(request, 'Password changed Successfully')
                return render(request, 'forgotpass.html')
        else:
            messages.info(request, mark_safe("Email does not exist, please <a href='signup'>Register</a> here"))
            return render(request, 'forgotpass.html')
    else:       
        return render(request, 'forgotpass.html')

def registeruser(request):

    if(request.method=='POST'):
        uname = request.POST['uname']
        email = request.POST['mail']
        password = request.POST['psw']
        repeatpass= request.POST['psw-repeat']
        
        if(User.objects.filter(email = email).exists()):
            messages.info(request, mark_safe("Email already exists, please <a href='login'>Login</a>"))
            return redirect('signup')

        if(password!=repeatpass):
            messages.info(request, 'potti munda password chusko')
            return redirect('signup')
        
        else:
            user = User.objects.create_user(username=uname, email=email, password=password)
            user.save()
            return render(request, 'success.html')

    else:
        return render(request, 'signup.html')

def help(request):
    return render(request, 'help.html')

def help2(request):
    return render(request, 'help2.html')

def contact(request):
    return render(request, 'contact.html')