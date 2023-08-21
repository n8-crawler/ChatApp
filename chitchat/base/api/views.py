from rest_framework.decorators import api_view, permission_classes,authentication_classes
from rest_framework.response import Response
from base.models import Room
from base.api import serializers
from .serializers import Roomserializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getrooms(request):
    datas = {'hi':'its ranjan'}
    rooms = Room.objects.all()
    serializers = Roomserializers(rooms,many=True)
    return Response(serializers.data)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def getroom(request,pk):

    room = Room.objects.get(id=pk)
    serializers = Roomserializers(room)
    return Response(serializers.data)
