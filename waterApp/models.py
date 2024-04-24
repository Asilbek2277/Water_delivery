from django.contrib.auth.models import User
from django.db import models


class Suv(models.Model):
    brend=models.CharField(max_length=200)
    narx=models.PositiveSmallIntegerField()
    litr=models.PositiveSmallIntegerField()
    batafsil=models.TextField()

class Mijoz(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    manzil=models.TextField()
    qarz=models.PositiveSmallIntegerField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)

class Admin(models.Model):
    ism=models.CharField(max_length=30)
    yosh=models.PositiveSmallIntegerField()
    ish_vaqti=models.CharField(max_length=200)
    user=models.ForeignKey(User, on_delete=models.CASCADE)


class Haydovchi(models.Model):
    ism=models.CharField(max_length=50)
    tel=models.CharField(max_length=20)
    kiritilgan_sana=models.DateTimeField()

class Buyurtma(models.Model):
    suv=models.ForeignKey(Suv, on_delete=models.CASCADE)
    sana=models.DateTimeField()
    mijoz=models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor=models.PositiveSmallIntegerField()
    umumiy_summa=models.PositiveBigIntegerField()
    admin=models.ForeignKey(Admin, on_delete=models.CASCADE)
    haydovchi=models.ForeignKey(Haydovchi, on_delete=models.CASCADE)


