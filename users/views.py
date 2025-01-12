from django.http import HttpResponse
from django.shortcuts import render
from django.middleware.csrf import get_token
from django.http import JsonResponse
from djoser.views import UserViewSet
from rest_framework.permissions import AllowAny

def index(request):
    return render(request, 'users/home.html')  # Render the home.html template
def get_csrf_token(request):
    return JsonResponse({"csrfToken": get_token(request)})

def test(request):
    return JsonResponse({"hello":"myhwllo"})

class CustomUserViewSet(UserViewSet):
    permission_classes = [AllowAny]  # Ensure public access