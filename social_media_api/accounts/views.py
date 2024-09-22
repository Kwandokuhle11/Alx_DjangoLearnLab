from argparse import Action
from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken

from accounts.models import CustomUser
from .serializers import RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    @Action(detail=True, methods=['post'])
    def follow(self, request, pk=None):
        user = self.get_object()
        request.user.follow(user)
        return Response({'status': f'You are now following {user.username}'})

    @Action(detail=True, methods=['post'])
    def unfollow(self, request, pk=None):
        user = self.get_object()
        request.user.unfollow(user)
        return Response({'status': f'You have unfollowed {user.username}'})