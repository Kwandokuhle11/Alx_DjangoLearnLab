from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
from .views import FollowUserView, UnfollowUserView

urlpatterns = [
    path('', include(router.urls)),
    path('users/<int:pk>/follow/', UserViewSet.as_view({'post': 'follow'})),
    path('users/<int:pk>/unfollow/', UserViewSet.as_view({'post': 'unfollow'})),
    path('users/<int:user_id>/follow/', FollowUserView.as_view(), name='follow-user'),
    path('users/<int:user_id>/unfollow/', UnfollowUserView.as_view(), name='unfollow-user'),
]
