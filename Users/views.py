from django.shortcuts import render ,redirect
from django.contrib import messages
from .forms import UserRegisterForm,UserProfileForm,UserUpdateForm
from django.contrib.auth import authenticate ,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Your Account has been successfully created! please login ')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'Users/register.html', {'form':form})


def Userlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user=authenticate(request, username=username ,password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome {username}')
            return redirect('index')
        else:
            messages.error(request, f'Enter correct Email and Password')
            return redirect('login')
    else:
        return render(request,'Users/login.html')


def Userlogout(request):
    logout(request)
    return render(request, 'logout.html')


@login_required(login_url='/login/')
def profile(request):
    if request.method=='POST':
        U_form=UserUpdateForm( request.POST, instance=request.user)
        P_form=UserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if U_form.is_valid() and P_form.is_valid():
            U_form.save()
            P_form.save()
    else:
        U_form=UserUpdateForm(instance=request.user)
        P_form=UserProfileForm(instance=request.user.profile)
    content={
        'u_form':U_form,
        'p_form':P_form,
    }
    return render(request ,'profile.html',content)
