from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
@api_view(['GET'])
def home(request):
    data = {
        "app": "halthcare management system"
        ,"version": "1.0.0"
    }
    return Response(data)

def index(request):
    return render(request, 'index.html')