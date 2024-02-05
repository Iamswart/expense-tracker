from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from .models import Budget
from .serializers import BudgetSerializer
from permissions.is_owner import IsOwner


class BudgetViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user-specific budgets.
    """
    serializer_class = BudgetSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        # Check if the request is part of generating Swagger documentation
        if getattr(self, 'swagger_fake_view', False):
            return Budget.objects.none()

        return Budget.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        """
        Assign the authenticated user as the owner of the budget.
        """
        serializer.save(user=self.request.user)
