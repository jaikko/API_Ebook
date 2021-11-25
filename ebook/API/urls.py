from django.urls import path, include, re_path

from API.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

from rest_framework_nested import routers

router = routers.DefaultRouter()
router.register(r'book', BookView, basename="Book")
# contract_routeur = routers.NestedSimpleRouter(router, r'clients', lookup='client')


urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('', include(router.urls)),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('user/', UserView.as_view({'get': 'list'}), name='user'),
]