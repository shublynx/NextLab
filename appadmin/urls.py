from django.urls import path
from appadmin import views


urlpatterns = [
    path("login/appadmin/",views.index),


]