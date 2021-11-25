from django.http import request
from rest_framework import permissions, views
from .models import *
import requests

class IsConnected(permissions.BasePermission):
 
    def has_permission(self, request, view):
        res = requests.post("http://127.0.0.1:8001/islogin/")
        if res == False:
            return False
        return True