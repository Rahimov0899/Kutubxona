from django.db import models

class Profil(models.Model):
    ism_fam=models.CharField(max_length=100)
    yosh=models.PositiveIntegerField(null=True)
    sana=models.DateField(auto_now=True)
    def __str__(self):
        return self.ism_fam

class Kurs(models.Model):
    tanlov=[('Boshlangich','Boshlangich'),('Orta','Orta'),('Yuqori','Yuqori')]
    nom=models.CharField(max_length=100)
    daraja=models.CharField(max_length=50,choices=tanlov)
    ustoz=models.CharField(max_length=70,verbose_name="ism familyasi")
    narx=models.PositiveBigIntegerField()
    chegirma=models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)
    matn = models.CharField(max_length=120,null=True)
    kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    baho = models.PositiveSmallIntegerField(null =True)
    def str(self):
        return self.matn

class Tanlangan(models.Model):
    kurs = models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil = models.ForeignKey(Profil,on_delete=models.CASCADE)

class Xarid(models.Model):
    tanlov = [("Boshlandi","Boshlandi"),("Korilyapti","Korilyapti"),("Tugadi","Tugadi")]
    kurs= models.ForeignKey(Kurs,on_delete=models.CASCADE)
    profil=models.ForeignKey(Profil,on_delete=models.CASCADE)
    sana = models.DateField(auto_now_add=True)
    holat = models.CharField(max_length=50,choices=tanlov)
    def __str__(self):
        return f"{self.kurs.nom},{self.profil.ism_fam}"

