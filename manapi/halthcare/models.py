from django.db import models
import uuid
# Create your models here.
class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    phone = models.CharField(max_length=50,blank=True)  
    gender = models.CharField(max_length=50,default="male")        
    specialization = models.CharField(max_length=50)
    hospital = models.CharField(max_length=300)
    department = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class Patient(models.Model):
    name = models.CharField(max_length=50) 
    age = models.IntegerField() 
    phone = models.CharField(max_length=50,blank=True)  
    gender = models.CharField(max_length=50,default="male")  
    medical_history = models.CharField(max_length=300)
    date_of_birth = models.DateField()
    blood_group = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
     
    def __str__(self):
        return self.name

def genrate_map_id():
    return str(uuid.uuid4()).split("-")[0].upper()
    
class Mapping(models.Model):
    mapping_id = models.CharField(max_length=50,default=genrate_map_id,unique=True)
    patient = models.ForeignKey(Patient,on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor,on_delete=models.CASCADE)
    remarks = models.CharField(max_length=300)            