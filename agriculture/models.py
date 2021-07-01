from django.db import models

# Create your models here.

class register(models.Model):
    name = models.CharField(max_length=40)
    phone = models.TextField(max_length=10)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=50)

class adminpanel(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='newfolder')
    desc = models.TextField()
    
    
class adminfruits(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='newfolder')
    desc = models.TextField()

class admintubers(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='newfolder')
    desc = models.TextField()

class adminveg(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='newfolder')
    desc = models.TextField()

class admingreens(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='newfolder')
    desc = models.TextField()

class soil(models.Model):
    soiltype = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    img = models.ImageField(upload_to='newfolder')

class Red(models.Model):
    img = models.ImageField(upload_to='newfolder')
    name = models.CharField(max_length=20)

class Sandy(models.Model):
    img = models.ImageField(upload_to='newfolder')
    name = models.CharField(max_length=20)

class Alluvial(models.Model):
    img = models.ImageField(upload_to='newfolder')
    name = models.CharField(max_length=20)

class Black(models.Model):
    img = models.ImageField(upload_to='newfolder')
    name = models.CharField(max_length=20)

class Clay(models.Model):
    img = models.ImageField(upload_to='newfolder')
    name = models.CharField(max_length=20)

class Dummy(models.Model):
    fname = models.CharField(max_length=15)
    lname = models.CharField(max_length=10)