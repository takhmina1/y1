# from django.db import models
# # from django.contrib.auth.models import User
# from django.conf import settings



# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     bio = models.TextField(blank=True)
#     profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

#     def __str__(self):
#         return self.user.username

# class Video(models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE)
#     upload_date = models.DateTimeField(auto_now_add=True)
#     video_file = models.FileField(upload_to='videos/')
#     likes = models.ManyToManyField(User, related_name='video_likes', blank=True)
#     dislikes = models.ManyToManyField(User, related_name='video_dislikes', blank=True)
#     views = models.PositiveIntegerField(default=0)
#     category = models.ForeignKey('VideoCategory', on_delete=models.SET_NULL, null=True, blank=True)

#     def __str__(self):
#         return self.title

#     def increment_views(self):
#         self.views += 1
#         self.save()

# class Comment(models.Model):
#     video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.TextField()
#     pub_date = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f"{self.user.username} - {self.text[:20]}"

# class Subscription(models.Model):
#     subscriber = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscriptions')
#     channel = models.ForeignKey(User, on_delete=models.CASCADE, related_name='subscribers')

#     def __str__(self):
#         return f"{self.subscriber.username} -> {self.channel.username}"

# class VideoCategory(models.Model):
#     name = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name

# class Playlist(models.Model):
#     title = models.CharField(max_length=100)
#     owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='playlists')
#     videos = models.ManyToManyField(Video, related_name='included_in_playlist', blank=True)

#     def __str__(self):
#         return f"{self.title} - {self.owner.username}"


from django.db import models
from django.conf import settings

class UserProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True)

    def __str__(self):
        return self.user.username

class Video(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploaded_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    upload_date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='video_likes', blank=True)
    dislikes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='video_dislikes', blank=True)
    views = models.PositiveIntegerField(default=0)
    category = models.ForeignKey('VideoCategory', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def increment_views(self):
        self.views += 1
        self.save()

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.text[:20]}"

class Subscription(models.Model):
    subscriber = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    channel = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscribers')

    def __str__(self):
        return f"{self.subscriber.username} -> {self.channel.username}"

class VideoCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Playlist(models.Model):
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='playlists')
    videos = models.ManyToManyField(Video, related_name='included_in_playlist', blank=True)

    def __str__(self):
        return f"{self.title} - {self.owner.username}"
