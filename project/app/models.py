from django.db import models

# Create your models here.
class Register(models.Model):
    medical_name=models.CharField(max_length=30)
    phone_name=models.CharField(max_length=30)
    phone_no=models.IntegerField()
    address=models.CharField(max_length=100)

    def __str__(self):
        return self.medical_name
    
