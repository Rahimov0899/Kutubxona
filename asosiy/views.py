from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

# def talabalar(request):
#     soz=request.GET.get('qidiruv')
#     if soz=="" or soz is None:
#          content = {
#         "talabalar":Talaba.objects.all()
#     }
#     else:
#         content = {
#         "talabalar":Talaba.objects.filter(ism__contains=soz)
#     }
#     return render(request,"",content)
# def talaba(request,son):
#     Talaba.objects.get(id=son).delete()
#
#     return redirect("/talaba/")

def kitob(request):
    nom=request.GET.get('qidiruv')
    if nom=="" or nom is None:
        content={
            "kitoblar":Kitob.objects.all()
    }
    else:
        content={
            "kitoblar":Kitob.objects.filter(nom__contains=nom)
    }
    return render(request,"kitob.html",content)

def kitoblar(request,id):
    Kitob.objects.get(id=id).delete()

    return redirect("/")

def recordlar(request):
        content={
           "record":Record.objects.all()
        }
        return render(request,"Record.html",content)

def record(request,id):
    Record.objects.get(id=id).delete()
    return redirect("/record/")

def mualliflar(request):
    ism=request.GET.get('qidiruv')
    if ism=="" or ism is None:
        content={
            "muallif":Muallif.objects.all()
        }
    else:
        content={
            "muallif":Muallif.objects.filter(ism__contains=ism)
    }
    return render(request,"muallif.html",content)

# def mualliflar(request):
#     content = {
#                 "muallif":Muallif.objects.all()
#             }
#     return render(request,"Mualliflar.html",content)
#
# def muallif(request,id):
#     Muallif.objects.get(id=id).delete()
#
#     return redirect("/hama_muallif/")

def muallif(request):
    content={
        "muallif":Muallif.objects.order_by("-tugilgan_yil")[:3]
        }
    return render(request,"Record.html",content)
