from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('talaba/', talabalar),
    path('bitta_ochir/<int:id>/',talaba ),
    path('muallif/', mualliflar),
    path('bitta_ochir/<int:id>/',muallif ),
    path('kitob/', kitob),
    path('bitta_ochir/<int:id>/',kitoblar ),
    path('record/', recordlar),
    path('bitta_ochir/<int:id>/',record ),
    path('adminlar/', adminlar),
    path('bitta_ochir/<int:id>/',adminn ),

 ]

