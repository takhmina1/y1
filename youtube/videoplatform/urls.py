from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    UserProfileViewSet, VideoViewSet, CommentViewSet,
    SubscriptionViewSet, VideoCategoryViewSet, PlaylistViewSet,
    TrendingVideosView, UserVideosView
)

# Создаем экземпляр DefaultRouter
router = DefaultRouter()

# Регистрируем viewsets в router
router.register(r'user-profiles', UserProfileViewSet, basename='userprofile')
router.register(r'videos', VideoViewSet, basename='video')
router.register(r'comments', CommentViewSet, basename='comment')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscription')
router.register(r'video-categories', VideoCategoryViewSet, basename='videocategory')
router.register(r'playlists', PlaylistViewSet, basename='playlist')

# Определяем URL-маршруты для TrendingVideosView и UserVideosView
urlpatterns = [
    path('trending-videos/', TrendingVideosView.as_view(), name='trending-videos'),
    path('user-videos/', UserVideosView.as_view(), name='user-videos'),
]

# Включаем URL-маршруты из router
urlpatterns += router.urls
