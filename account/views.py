from rest_framework import viewsets

from account.models import User
from account.serializers import UserWriteSerializer, UserViewSerializer


# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return UserWriteSerializer
        else:
            return  UserViewSerializer