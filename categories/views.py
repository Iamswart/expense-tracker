from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdminOrReadOnly 

class CategoryViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing category instances.
    - Allows unrestricted access to list and retrieve actions.
    - Creation, update, and deletion are restricted to admin users.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminOrReadOnly]