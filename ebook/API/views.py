import django_filters
from django_filters.filters import CharFilter
from rest_framework import viewsets, permissions, generics
from .permissions import IsConnected
from .models import Book, User, Category
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    BookSerializer,
    CategorySerializer
)


# Create your views here.
class BookFilter(django_filters.FilterSet):
    title = CharFilter(lookup_expr='icontains')
    category = CharFilter(field_name='category__name', lookup_expr='exact')

    class Meta:
        model = Book
        fields = ['title', 'category']


class CategoryView(viewsets.ModelViewSet):

    permission_classes = [IsConnected]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BookView(viewsets.ModelViewSet):

    permission_classes = [IsConnected]
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_class = BookFilter


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
