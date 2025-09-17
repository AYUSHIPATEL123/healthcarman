from django.contrib import admin
from .models import *
# Register your models here.

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id','name','specialization','phone','age','gender','hospital','department')
    list_filter = ('specialization','age','gender','hospital','department')

class PatientAdmin(admin.ModelAdmin):
    list_display = ('id','name','age','gender','phone','medical_history','date_of_birth','blood_group','city','state')
    list_filter = ('age','gender','blood_group','city','state')    
    
class MappingAdmin(admin.ModelAdmin):
    list_display = ('id','mapping_id','doctor','patient')
    list_filter = ('doctor',)



admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Patient,PatientAdmin)
admin.site.register(Mapping,MappingAdmin)            