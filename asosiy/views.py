import requests
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *

def talabalar(request):
    if request.method=='POST':
        Talaba.objects.create(
        ism=request.POST['i'],
        kurs=request.POST.get('k'),
        kitob_soni=request.POST.get('k_s')
    )
        return redirect("/talaba/")
    soz=request.GET.get('qidiruv')
    if soz=="" or soz is None:
         content = {
        "talabalar":Talaba.objects.all()
    }
    else:
        content = {
        "talabalar":Talaba.objects.filter(ism__contains=soz)
    }
    return render(request,"muallif.html",content)
def talaba(request,id):
    Talaba.objects.get(id=id).delete()

    return redirect("/talaba/")

def kitob(request):
    if request.method=='POST':
        Kitob.objects.create(
            nom=request.POST.get('nomi'),
            sahifa=request.POST.get('s'),
            janr=request.POST.get('j'),
            muallif=Muallif.objects.get(id=request.POST.get('m')),
            yaratilgan_sana=request.POST.get('y'),
            tahrirlangan_sana=request.POST.get('t')
        )
        return redirect("/kitob/")
    nom=request.GET.get('qidiruv')
    if nom=="" or nom is None:
        content={
            "kitoblar":Kitob.objects.all(),
            "mualliflar": Muallif.objects.all()
    }
    else:
        content={
            "kitoblar":Kitob.objects.filter(nom__contains=nom)
    }
    return render(request,"Record.html",content)

def kitoblar(request,id):
    Kitob.objects.get(id=id).delete()

    return redirect("kitob")

def recordlar(request):
    if request.method=='POST':
        Record.objects.create(
            talaba=Talaba.objects.get(id=request.POST.get('talaba')),
            olingan_sana=request.POST.get('s_o'),
            qaytarish_sana=request.POST.get('q_s'),
            kitob=Kitob.objects.get(id=request.POST.get('kitob')),
            admin=Admin.objects.get(id=request.POST.get('admin'))

        )
        return redirect("/record/")
    soz=request.GET.get('qidiruv')
    if soz=='' or soz is None:
       content={
           "recordlar":Record.objects.all(),
           "talabalar":Talaba.objects.all(),
           "kitoblar":Kitob.objects.all(),
           "adminlar":Admin.objects.all()
        }
    else:

        content={
            "recordlar":Record.objects.filter(talaba__contains=soz)
        }
    return render(request,"record2.html",content)


def record(request,id):
    Record.objects.get(id=id).delete()
    return redirect("/record/")

def mualliflar(request):
    if request.method=='POST':
        Muallif.objects.create(
        ism=request.POST['i'],
        kitob_soni=request.POST.get('k'),
        jins=request.POST.get('j'),
        trik=request.POST.get('t'),
        tugilgan_yil=request.POST.get('t_y')
    )
        return redirect("/muallif/")
    ism=request.GET.get('qidiruv')
    if ism=="" or ism is None:
        content={
            "muallif":Muallif.objects.all()
        }
    else:
        content={
            "muallif":Muallif.objects.filter(ism__contains=ism)
    }
    return render(request,"Mualliflar.html",content)



def muallif(request,id):
    Muallif.objects.get(id=id).delete()

    return redirect("/muallif/")

def adminlar(request):
    if request.method=='POST':
        Admin.objects.create(
            ism=request.POST.get('ism'),
            familiya=request.POST.get('fam'),
            ish_vaqt=request.POST.get('vaqt')

        )
        return redirect("/adminlar/")
    soz=request.GET.get('qidiruv')
    if soz=='' or soz is None:
       content={
           "adminlar":Admin.objects.all()
        }
    else:

        content={
            "adminlar":Admin.objects.filter(talaba__contains=soz)
        }
    return render(request,"amdin.html",content)


def adminn(request,id):
    Admin.objects.get(id=id).delete()
    return redirect("/adminlar/")

