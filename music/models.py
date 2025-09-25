from django.db import models

# Create your models here.
class Smusic(models.Model):
    songid=models.IntegerField(primary_key=True)
    songname=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    singername=models.CharField(max_length=30)
    song=models.FileField(upload_to='songs/')
    image=models.FileField(upload_to='images/',null=True)


class Like(models.Model):
    songid=models.IntegerField(primary_key=True)
    songname=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    singername=models.CharField(max_length=30)
    song=models.FileField(upload_to='songs/')
    image=models.FileField(upload_to='images/',null=True)



class Pmusic(models.Model):
    songid=models.IntegerField(primary_key=True)
    songname=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    singername=models.CharField(max_length=30)
    song=models.FileField(upload_to='songs/')
    image=models.FileField(upload_to='images/')


class Fmusic(models.Model):
    songid=models.IntegerField(primary_key=True)
    songname=models.CharField(max_length=30)
    moviename=models.CharField(max_length=30)
    genre=models.CharField(max_length=30)
    singername=models.CharField(max_length=30)
    song=models.FileField(upload_to='songs/')
    image=models.FileField(upload_to='images/')


class Singers(models.Model):
    singerid=models.IntegerField(primary_key=True)
    singername=models.CharField(max_length=30)
    image=models.FileField(upload_to='images/')
    genre=models.CharField(max_length=30)
