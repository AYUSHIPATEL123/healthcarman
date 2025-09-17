from django.shortcuts import render
from .serializers import RegisterSerializer,LoginSerializer,DoctorSerializer,PatientSerializer,MappingSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated , AllowAny
from django.contrib.auth.models import User
from .models import Doctor , Patient , Mapping
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# Create your views here.

class RegisterViewSet(viewsets.ModelViewSet):   # to create user
    serializer_class = RegisterSerializer 
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    
class LoginView(APIView): # to login
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]    # to allow any user
    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():   # if serializer is not valid
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=serializer.validated_data['username'],password=serializer.validated_data['password']) # to authenticate
        if user:  
            refresh =  RefreshToken.for_user(user)   # to create refresh token
            return Response({"daat":serializer.data,'refresh':str(refresh),'access':str(refresh.access_token)},status=status.HTTP_200_OK)  # to return response with access token
        else:
            return Response({"error":"invalid credentials"},status=status.HTTP_400_BAD_REQUEST)
    
class DoctorViewSet(viewsets.ModelViewSet):
    serializer_class = DoctorSerializer   # to serialize data
    queryset = Doctor.objects.all()
    permission_classes = [IsAuthenticated]  # to allow only authenticated user

class PatientViewSet(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()
    permission_classes = [IsAuthenticated]

class MappingViewSet(viewsets.ModelViewSet):
    serializer_class = MappingSerializer
    queryset = Mapping.objects.all()
    permission_classes = [IsAuthenticated]        