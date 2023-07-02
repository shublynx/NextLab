from django.shortcuts import render
from .models import AdminModel,Category,Subcategory
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
        appname = request.POST['appname']
        applink = request.POST['applink']
        category = request.POST['category']
        subcategory = request.POST['subcategory']
        points = request.POST['points']

        appmodel = AdminModel(appname=appname,applink=applink,category=category,subcategory=subcategory,points=points)
        appmodel.save()


