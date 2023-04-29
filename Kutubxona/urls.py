from django.contrib import admin
from django.urls import path
from asosiy.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('talaba/',talabalar ),
    # path('talaba_ochir/<int:son>/', talaba),
    path('', kitob),
    path('kitob_ochir/<int:id>/', kitoblar),
    path('hama_muallif/', mualliflar),
    # path('hama_ochirish/<int:id>/', muallif),
    path('record/', recordlar),
    path('bitta_ochir/<int:id>/', record),
    path('muallif/',muallif ),
]

