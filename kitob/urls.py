
from django.contrib import admin
from django.urls import path
from app1.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', salomlash),
    path('men/', men),
    path('loyiha/', loyiha),
    path('asosiy/', asosiy),
    path('kitob/', Kitoblar),
    path('student/', Studentlar),
    path('muallif/', mualliflar),
    path('kitoblar/<int:son>/', kitob_ochir),
    path('studentlar/<int:son>/',student_ochir),
    path('record/',record),
    path('kitob_edit/<int:p>/',kitob_edit),
    path('muallif_edit/<int:p>/',muallif_edit),



]
