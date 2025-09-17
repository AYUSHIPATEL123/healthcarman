from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Doctor , Patient , Mapping
class RegisterSerializer(serializers.ModelSerializer): # serializer
    class Meta:
        model = User     # user model
        fields = ['first_name', 'last_name', 'username', 'email', 'password']   # fields
        extra_kwargs = {
            'password': {'write_only': True}
        }    # to hide password
    def validate(self,data):
        if User.objects.filter(email=data['email']).exists():   # to check if email already exists
            raise serializers.ValidationError("Email already exists")
        if User.objects.filter(username=data['username']).exists():  # to check if username already exists
            raise serializers.ValidationError("Username already exists")
        if len(data['password'])<8: # to check if password is at least 8 characters
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return data
    
    def create(self, validated_data):     # to create user
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        if not user:
            raise serializers.ValidationError("User could not be created")
        user.save()
        return user
    
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()    

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'   # all fields

class PatientSerializer(serializers.ModelSerializer):
    date_of_birth = serializers.DateField(format="%Y-%m-%d")
    class Meta:
        model = Patient
        fields = ['id','name','age','phone','gender','medical_history','date_of_birth','blood_group','city','state']        # specific fields

class MappingSerializer(serializers.ModelSerializer):
    doctor_details = DoctorSerializer(source='doctor',read_only=True)
    patient_details = PatientSerializer(source='patient',read_only=True)
    class Meta:
        model = Mapping
        fields = ['id','mapping_id','doctor','patient','remarks','doctor_details','patient_details'] 
           