from django.db import models
class Muallif(models.Model):
    ism=models.CharField(max_length=30)
    tirik=models.BooleanField(default=True)
    yosh=models.PositiveSmallIntegerField()
    kitoblar_soni=models.PositiveSmallIntegerField(blank=True)
    def __str__(self):
        return self.ism
class kitob(models.Model):
    nom=models.CharField(max_length=30)
    sana=models.DateField(blank=True)
    sahifa=models.PositiveSmallIntegerField()
    janr=models.CharField(max_length=30,choices=(("1","Fantastik"),("2","Hujiatli"),("3","Badiy")))
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE,related_name="m_k")
    def __str__(self):
        return self.nom
class student(models.Model):
    ism = models.CharField(max_length=30)
    guruh = models.CharField(max_length=30,blank=True)
    bitiruvchi = models.BooleanField(default=False)
    kitoblar_soni = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.ism
class Record(models.Model):
    student=models.ForeignKey(student,on_delete=models.CASCADE,related_name="s")
    kitob=models.ForeignKey(kitob,on_delete=models.CASCADE,related_name="k")
    sana=models.DateField(auto_now_add=True)
    qaytardi=models.CharField(max_length=7,blank=True,default="yoq")
    qaytarish_sana=models.DateField(blank=True,null=True)
    def __str__(self):
        return f"{self.student}{self.kitob}"
