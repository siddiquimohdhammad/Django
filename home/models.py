from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email=models.CharField(max_length=122)
    num = models.CharField(max_length=12, null=True, blank=True)
    desc=models.TextField(max_length=122)
    date = models.DateField(auto_now_add=True)

    


    def __str__(self):
        return self.name

class Product(models.Model):
    a=models.CharField(max_length=20)
    b=models.CharField(max_length=20)
    date = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.a



