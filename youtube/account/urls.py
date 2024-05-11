from django.urls import path
from account.views import RegistrationAPIView

urlpatterns = [
    path('api/register/', RegistrationAPIView.as_view(), name='registration'),
    # Другие URL-пути вашего приложения
]
