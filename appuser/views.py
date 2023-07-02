from django.shortcuts import render,redirect
from appadmin.models import AdminModel
from appuser.models import CustomUser
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def home(request):

    return render(request,'auth/home.html')


def detail(request,id):

    appdetail = AdminModel.objects.get(id=id)
    return render(request,'appuser/detail.html',{'appdetail':appdetail})



def register(request):

    if request.method == 'POST':
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        user = CustomUser.objects.create_user(username=username, password=password, email=email)

        user.save()

        return redirect('/')
    return render(request, 'auth/register.html')

def user_login(request):

    apps = AdminModel.objects.all()

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        # Authenticate and login the user
        user = authenticate(username=username,password=password)

        if user is not None:
            login(request, user)
            if user.is_superuser:
                return redirect('appadmin/')
            else:
                return render(request,'appuser/index.html',{'apps':apps})


        else:
            return render(request,'auth/login.html',{ 'error' : 'Invalid Credentials'})
    return render(request,'auth/login.html')


def user_logout(request):
    if request.method == 'POST':
        logout(request)
    return redirect("/")
