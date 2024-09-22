from argparse import Action
from django.shortcuts import render

# Create your views here.
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .models import CustomUser
from .serializers import UserSerializer

# Follow View
class FollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_follow = get_object_or_404(CustomUser, id=kwargs['user_id'])
        request.user.follow(user_to_follow)
        return Response({"status": f"You are now following {user_to_follow.username}"}, status=status.HTTP_200_OK)

# Unfollow View
class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        user_to_unfollow = get_object_or_404(CustomUser, id=kwargs['user_id'])
        request.user.unfollow(user_to_unfollow)
        return Response({"status": f"You have unfollowed {user_to_unfollow.username}"}, status=status.HTTP_200_OK)
