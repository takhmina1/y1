from rest_framework import viewsets, generics, permissions, status
from rest_framework.response import Response
from .models import UserProfile, Video, Comment, Subscription, VideoCategory, Playlist
from .serializers import UserProfileSerializer, VideoSerializer, CommentSerializer, SubscriptionSerializer, VideoCategorySerializer, PlaylistSerializer
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated

# Создаем viewset для управления профилями пользователей
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserProfile.objects.filter(user=self.request.user)

# Создаем viewset для управления видео
class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Добавляем дополнительные действия для лайков, дизлайков и комментариев
    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        video = self.get_object()
        video.likes.add(request.user)
        return Response({'status': 'liked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def dislike(self, request, pk=None):
        video = self.get_object()
        video.dislikes.add(request.user)
        return Response({'status': 'disliked'}, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def comment(self, request, pk=None):
        video = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user, video=video)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Создаем viewset для управления комментариями
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Создаем viewset для управления подписками
class SubscriptionViewSet(viewsets.ModelViewSet):
    queryset = Subscription.objects.all()
    serializer_class = SubscriptionSerializer
    permission_classes = [IsAuthenticated]

    # Переопределяем метод perform_create для сохранения подписчика при создании подписки
    def perform_create(self, serializer):
        serializer.save(subscriber=self.request.user)

# Создаем viewset для управления категориями видео
class VideoCategoryViewSet(viewsets.ModelViewSet):
    queryset = VideoCategory.objects.all()
    serializer_class = VideoCategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

# Создаем viewset для управления плейлистами
class PlaylistViewSet(viewsets.ModelViewSet):
    queryset = Playlist.objects.all()
    serializer_class = PlaylistSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    # Переопределяем метод perform_create для сохранения владельца при создании плейлиста
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# Добавляем дополнительные generic views для более сложных операций
# Показываем топ-10 видео по просмотрам
class TrendingVideosView(generics.ListAPIView):
    queryset = Video.objects.order_by('-views')[:10]
    serializer_class = VideoSerializer
    permission_classes = [permissions.AllowAny]

# Показываем видео пользователя
class UserVideosView(generics.ListAPIView):
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Video.objects.filter(uploaded_by=self.request.user)
