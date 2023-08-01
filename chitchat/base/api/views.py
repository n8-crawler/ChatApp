from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from base.api import serializers
from .serializers import Roomserializers

@api_view(['GET'])
def getrooms(request):
    datas = {'hi':'its ranjan'}
    rooms = Room.objects.all()
    serializers = Roomserializers(rooms,many=True)
    return Response(serializers.data)


@api_view(['GET'])
def getroom(request,pk):
    room = Room.objects.get(id=pk)
    serializers = Roomserializers(room)
    return Response(serializers.data)
