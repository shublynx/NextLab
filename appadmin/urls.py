from django.urls import path
from appadmin import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("login/appadmin/",views.adminhome),
    path("login/appadmin/points",views.addapps),
    path("/",views.save_app,name='save_app'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)