import datetime
from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
# Create your views here.
from rest_framework.decorators import api_view, renderer_classes, permission_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response

from api.serializer import UserSerializer

@permission_classes((permissions.AllowAny,))
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET'])
@renderer_classes((JSONRenderer,))
@permission_classes((permissions.AllowAny,))
def get_date(request):
    return Response({'hora_actual': datetime.datetime.now().isoformat()})