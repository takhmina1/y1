from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserProfileViewSet, VideoViewSet, CommentViewSet, SubscriptionViewSet, VideoCategoryViewSet, PlaylistViewSet, TrendingVideosView, UserVideosView

# Создаем router для автоматической генерации URL-паттернов на основе viewsets
router = DefaultRouter()
router.register(r'user-profiles', UserProfileViewSet)
router.register(r'videos', VideoViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'video-categories', VideoCategoryViewSet)
router.register(r'playlists', PlaylistViewSet)

# Определяем URL-паттерны для generics views
urlpatterns = [
    path('trending-videos/', TrendingVideosView.as_view(), name='trending-videos'),
    path('user-videos/', UserVideosView.as_view(), name='user-videos'),
]

# Включаем URL-паттерны viewsets из router
urlpatterns += router.urls
