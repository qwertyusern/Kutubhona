from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
from .forms import *
def salomlash(request):
    return render(request,"salomlash.html")
def men(request):
    return render(request,"men.html")
def loyiha(request):
    return render(request,"loyiha.html")
def asosiy(request):
    return render(request,"asosiy.html")
def Kitoblar(request):
    if request.method == "POST":
        f = Kitobform(request.POST)
        if f.is_valid():
            f.save()
        return redirect("/kitob/")
    soz= request.GET.get("qidirish")
    m = Muallif.objects.all()
    if soz==None:
        k=kitob.objects.all().order_by("nom")
    else:
        k = kitob.objects.filter(nom=soz)
    f=Kitobform()
    return render(request,"books.html",{"kitoblar":k,"muallif":m,"form":f})
def Studentlar(request):
    if request.method=="POST":
        f=Studentform(request.POST)
        if f.is_valid():
            student.objects.create(
                ism=f.cleaned_data.get("ism"),
                guruh=f.cleaned_data.get("guruh"),
                bitiruvchi=f.cleaned_data.get("bitiruvchi"),
                kitoblar_soni=f.cleaned_data.get("kitoblar_soni")
        )
        return redirect("/student/")
    f=Studentform()
    soz = request.GET.get("qidirish")
    if soz == None:
        s = student.objects.all().order_by("ism")
    else:
        s = student.objects.filter(ism=soz)
    return render(request,"studentlar.html",{"studentlar":s, "form":f})
def mualliflar(request):
    if request.method == "POST":
        f = Muallifform(request.POST)
        if f.is_valid():
            Muallif.objects.create(
                ism=f.cleaned_data.get("ism"),
                tirik=f.cleaned_data.get("tirik"),
                bitiruvchi=f.cleaned_data.get("bitiruvchi"),
                kitoblar_soni=f.cleaned_data.get("kitoblar_soni")
            )
        return redirect("/muallif/")
    f=Muallifform
    m=Muallif.objects.all().order_by("ism")
    return render(request,"muallif.html",{"muallif":m,"form":f})
def kitob_ochir(request,son):
    kitob.objects.get(id=son).delete()
    return redirect("/kitob/")
def student_ochir(request,son):
    student.objects.get(id=son).delete()
    return redirect("/student/")
def record(request):
    r = Record.objects.all()
    f = Recordform()
    if request.method == "POST":
        f = Recordform(request.POST)
        if f.is_valid():
            f.save()
        return redirect("/record/")
    return render(request,"record.html",{"rec":r,"form":f})
def kitob_edit(request,p):
    if request.method=="POST":
        k=kitob.objects.get(id=p)
        k.nom=request.POST.get("nom")
        k.sana=request.POST.get("s")
        k.sahifa=request.POST.get("sahifa")
        k.janr=request.POST.get("j")
        k.muallif=Muallif.objects.get(id=request.POST.get("muallif"))
        k.save()
        return redirect("/kitob/")
    k1=kitob.objects.get(id=p)
    m=Muallif.objects.all()
    return render(request, "kitob-edit.html", {"kitob":k1,"muallif":m})
def muallif_edit(request,p):
    if request.method=="POST":
        m=Muallif.objects.get(id=p)
        m.ism=request.POST.get("ism")
        m.yosh=request.POST.get("y")
        m.kitoblar_soni=request.POST.get("k_s")
        m.save()
        return redirect("/muallif/")
    m1=Muallif.objects.get(id=p)
    return render(request, "kitob-edit.html", {"muallif":m1})