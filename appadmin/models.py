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
    apppic = models.ImageField(upload_to="Images/",default="Images/Noimg.jpg")
    appname = models.CharField(max_length=100)
    applink = models.URLField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    points = models.CharField(max_length=10)

    def __str__(self):
        return self.appname

