from django.http import HttpResponse
from django.shortcuts import render,redirect
from .models import *
def salomlash(request):
    return render(request,"salomlash.html")
def men(request):
    return render(request,"men.html")
def loyiha(request):
    return render(request,"loyiha.html")
def asosiy(request):
    return render(request,"asosiy.html")
def Kitoblar(request):
    if request.method=="POST":
        i = request.POST.get("muallif")
        m = Muallif.objects.get(id=i)
        kitob.objects.create(
            nom=request.POST.get("nom"),
            sana=request.POST.get("s"),
            sahifa=request.POST.get("sahifa"),
            janr=request.POST.get("j"),
            muallif=m
        )
        return redirect("/kitob/")
    soz= request.GET.get("qidirish")
    m = Muallif.objects.all()
    if soz==None:
        k=kitob.objects.all().order_by("nom")
    else:
        k = kitob.objects.filter(nom=soz)
    return render(request,"books.html",{"kitoblar":k,"muallif":m})
def Studentlar(request):
    if request.method=="POST":
        if request.POST.get("t")== False:
            natija=False
        else:
            natija=True
        student.objects.create(
            ism=request.POST.get("ismi"),
            guruh=request.POST.get("g"),
            bitiruvchi=natija,
            kitoblar_soni=request.POST.get("k_s")
        )
        return redirect("/student/")
    soz = request.GET.get("qidirish")
    if soz == None:
        s = student.objects.all().order_by("ism")
    else:
        s = student.objects.filter(ism=soz)
    return render(request,"studentlar.html",{"studentlar":s})
def mualliflar(request):
    if request.method=="POST":
        if request.POST.get("t")== False:
            natija=False
        else:
            natija=True
        Muallif.objects.create(
            ism=request.POST.get("ismi"),
            tirik=natija,
            yosh=request.POST.get("y"),
            kitoblar_soni=request.POST.get("k_s")
        )
        return redirect("/muallif/")
    m=Muallif.objects.all().order_by("ism")
    return render(request,"muallif.html",{"muallif":m})
def kitob_ochir(request,son):
    kitob.objects.get(id=son).delete()
    return redirect("/kitob/")
def student_ochir(request,son):
    student.objects.get(id=son).delete()
    return redirect("/student/")
def record(request):
    r = Record.objects.all()
    s=student.objects.all()
    k=kitob.objects.all()
    if request.method == "POST":
        i = request.POST.get("student")
        s = student.objects.get(id=i)
        u = request.POST.get("kitob")
        k = kitob.objects.get(id=u)
        Record.objects.create(
            student=s,
            kitob=k,
            sana=request.POST.get("sana")
        )
        return redirect("/record/")
    return render(request,"record.html",{"rec":r,"st":s,"kt":k})
def kitob_edit(request,p):
    if request.method=="POST":
        k=kitob.objects.get(id=p)
        k.nom=request.POST.get("nom")
        k.sana=request.POST.get("s")
        k.sahifa=request.POST.get("sahifa")
        k.janr=request.POST.get("j")
        k.muallif=kitob.objects.get(id=request.POST.get("muallif"))
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