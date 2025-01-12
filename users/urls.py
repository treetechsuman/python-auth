from django.urls import path,include
from rest_framework import permissions
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.conf.urls.static import static
from django.conf import settings

from django.views.decorators.csrf import csrf_exempt
from djoser.views import UserViewSet
from .views import CustomUserViewSet




from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path("auth/users/reset_password/", csrf_exempt(UserViewSet.as_view({"post": "reset_password"}))), 
    #path("auth/users/reset_password/", views.test, name='test'),
    path('auth/users/reset-password/', CustomUserViewSet.as_view({'post': 'reset_password'})),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')), 
    path("auth/csrf-token/", views.get_csrf_token),
    
]
urlpatterns += [
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)