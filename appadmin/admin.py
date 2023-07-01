from django.contrib import admin
from .models import Category,Subcategory,AdminModel

# Register your models here.
admin.site.register(Category)
admin.site.register(Subcategory)
admin.site.register(AdminModel)