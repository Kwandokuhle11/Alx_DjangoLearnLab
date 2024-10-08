from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FeedView, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = router.urls

from django.urls import path, include

urlpatterns = [
    path('api/', include('posts.urls')),
    path('feed/', FeedView.as_view(), name='feed'),
]
