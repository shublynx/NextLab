from django.urls import path
from appuser import views

urlpatterns = [
    path("",views.home,name='home'),
    path("login/appuser/",views.user_login,name='user_login'),
    path("<int:id>/",views.detail,name="detail"),

]