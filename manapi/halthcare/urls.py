from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import RegisterViewSet,LoginView,DoctorViewSet,PatientViewSet,MappingViewSet
from rest_framework_simplejwt.views import TokenObtainPairView ,TokenRefreshView

router = DefaultRouter()    # to create router
router.register('register',RegisterViewSet,basename='register')  # to register register viewsetclass
router.register('doctor',DoctorViewSet,basename='doctor')
router.register('patient',PatientViewSet,basename='patient')
router.register('mapping',MappingViewSet,basename='mapping')

urlpatterns = [
    path('login/',LoginView.as_view(),name='login'),    # to register login viewsetclass
    path('',include(router.urls)),
    path('token/',TokenObtainPairView.as_view(),name='token_obtain_pair'),   # get the token
    path('token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),  # refresh the token  
]
