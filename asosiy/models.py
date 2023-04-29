from django.db import models
class Talaba(models.Model):
    ism=models.CharField(max_length=100)
    kitob_soni=models.PositiveIntegerField()
    kurs=models.PositiveIntegerField()
    tugilgan_sana = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.ism

class Muallif(models.Model):
    Jinsi=[
        ('Erkak', 'Erkak'),
        ('Ayol','Ayol')
    ]
    ism=models.CharField(max_length=100)
    kitob_soni=models.PositiveIntegerField()
    jins=models.CharField(max_length=100, choices=Jinsi)
    trik=models.BooleanField()
    tugilgan_yil=models.DateField()

    def __str__(self):
        return self.ism

class Admin(models.Model):
    ism=models.CharField(max_length=100)
    familiya = models.CharField(max_length=100)
    ish_vaqt=models.DateField(auto_now_add=True)

    def __str__(self):
        return self.ism


class Kitob(models.Model):
    nom=models.CharField(max_length=100)
    muallif=models.ForeignKey(Muallif, on_delete=models.CASCADE)
    sahifa=models.PositiveIntegerField()
    janr=models.CharField(max_length=300)
    yaratilgan_sana = models.DateField()
    tahrirlangan_sana = models.DateField(auto_now=True)

    def __str__(self):
        return self.nom

class Record(models.Model):
    talaba=models.ForeignKey(Talaba, on_delete=models.CASCADE)
    kitob=models.ForeignKey(Kitob, on_delete=models.CASCADE)
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    olingan_sana=models.DateField()
    qaytarish_sana=models.DateField(blank=True,null=True)
    qaytardi=models.BooleanField(blank=True,null=True)
    qabul_qiluvchi = models.CharField(max_length=100,blank=True,null=True)
    berilgan_vaqt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.talaba)
