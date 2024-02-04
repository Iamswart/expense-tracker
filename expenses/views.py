from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework.exceptions import PermissionDenied
from permissions.is_owner import IsOwner

class ExpenseViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user-specific expenses.
    """
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            # Return an empty queryset for schema generation
            return Expense.objects.none()

        user = self.request.user
        if user.is_authenticated:
            return Expense.objects.filter(user=user)
        else:
            # Handle unauthenticated access attempts
            raise PermissionDenied("Authentication required")

    def perform_create(self, serializer):
        """
        Assign the authenticated user as the owner of the expense.
        """
        serializer.save(user=self.request.user)
