from django.db import models

class Register(models.Model):
    fname = models.CharField(max_length=50)
    uname = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=20)

def __str__(self):
    return "fname:"+self.fname+" uname:"+self.uname+"email:"+self.email

