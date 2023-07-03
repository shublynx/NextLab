from django.db import models

# Create your models here.

from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class AdminModel(models.Model):
    apppic = models.FileField(upload_to='appadmin/',max_length=250,default=None)
    appname = models.CharField(max_length=100)
    applink = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE,null=True)
    points = models.CharField(max_length=10)

    def __str__(self):
        return self.appname

