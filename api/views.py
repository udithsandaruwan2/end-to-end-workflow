from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.models import User
from .serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def getRoot(request):
    routes = [
        "/api/users/ - GET all users",
        "/api/token/ - Obtain JWT Token",
        "/api/token/refresh/ - Refresh JWT Token",
    ]
    return Response(routes)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_user_list(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)