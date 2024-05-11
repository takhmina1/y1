from django.contrib import admin
from django.urls import path, include
from .yasg import urlpatterns as yasg  # импортируем маршруты Swagger из файла yasg.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('videoplatform.urls')),
    path('api/', include('account.urls')),
    
    # Подключение маршрутов Swagger
    path('', include(yasg)),  # подключаем маршруты Swagger
]
