from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def home(request):
    data = {
        "app": "halthcare management system"
        ,"version": "1.0.0"
    }
    return Response(data)