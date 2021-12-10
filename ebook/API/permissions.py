from rest_framework import permissions
import requests


class IsConnected(permissions.BasePermission):

    def has_permission(self, request, view):
        res = requests.post("http://127.0.0.1:8001/islogin/")
        if not res:
            return False
        return True
