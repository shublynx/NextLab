from django.shortcuts import render,redirect
from .models import AdminModel,Category,Subcategory
from django.contrib import messages
# Create your views here.

def index(request):
    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request,'appadmin/indexx.html',{'categories':categories,'subcategories':subcategories})

def addapps(request):


    categories = Category.objects.all()
    subcategories = Subcategory.objects.all()

    return render(request, 'appadmin/addapps.html', {'categories': categories, 'subcategories': subcategories})


def adminhome(request):

    apps = AdminModel.objects.all()
    return render(request, 'appadmin/adminhome.html', {'apps': apps})


def save_app(request):

    if request.method == 'POST':
        apppic = request.FILES.get('imageUpload')
        appname = request.POST.get('appname')
        applink = request.POST.get('applink')
        category = request.POST.get('category')
        subcategory = request.POST.get('subcategory')
        points = request.POST.get('pointsInput')

        admin_model = AdminModel(
            apppic=apppic,
            appname=appname,
            applink=applink,
            category_id=category,
            subcategory_id=subcategory,
            points=points
        )
        admin_model.save()

        messages.success(request, 'App added successfully!')

        return redirect('login/appadmin/')


