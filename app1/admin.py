from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


@admin.register(Muallif)
class StudentAdmin(ModelAdmin):
    search_fields = ("id","ism")

@admin.register(kitob)
class StudentAdmin(ModelAdmin):
    list_display = ("nom","sahifa","janr")
    search_fields = ("id","nom","muallif")
    autocomplete_fields = ("muallif",)
@admin.register(student)
class StudentAdmin(ModelAdmin):
    search_fields = ("id", "ism")
@admin.register(Record)
class StudentAdmin(ModelAdmin):
    search_fields = ("id", "nom", "muallif","kitoblar")
    autocomplete_fields = ("student","kitob",)


