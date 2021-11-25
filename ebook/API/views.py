from django.http import request
from django.shortcuts import render
from rest_framework import viewsets, permissions, generics
from rest_framework.views import APIView

from .permissions import IsConnected
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
import requests

# Create your views here.

class BookView(viewsets.ModelViewSet):
   
    permission_classes = [IsConnected]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    

class UserView(viewsets.ModelViewSet):
   
    permission_classes = [IsConnected]
    serializer_class = UserSerializer
    def get_queryset(self):
        
        user = self.request.user
        return User.objects.filter(email=user)

        
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = []
    serializer_class = RegisterSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return User.objects.all()