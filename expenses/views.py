from django.db.models import Sum, F, Q
from django.utils import timezone
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Expense
from budgets.models import Budget
from categories.models import Category 
from .serializers import ExpenseSerializer
from permissions.is_owner import IsOwner 

class ExpenseViewSet(viewsets.ModelViewSet):
    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        if getattr(self, 'swagger_fake_view', False):
            return Expense.objects.none()
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class AnalyticsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        start_date = request.query_params.get('start_date', timezone.now().date())
        end_date = request.query_params.get('end_date', timezone.now().date())

        expenses = Expense.objects.filter(
            user=request.user,
            date__range=[start_date, end_date]
        ).values('category__name').annotate(total_expense=Sum('amount'))

        expenses_dict = {item['category__name']: item['total_expense'] for item in expenses}

        budgets = Budget.objects.filter(user=request.user).annotate(
            remaining_budget=F('amount') - Sum('category__expenses__amount', filter=(
                Q(category__expenses__date__range=[start_date, end_date]) &
                Q(category__expenses__user=request.user)
            ), distinct=True)
        ).values('category__name', 'amount', 'remaining_budget')

        response_data = {
            'total_expenses': sum(expenses_dict.values()),
            'expenses_by_category': list(expenses),
            'budgets_and_remaining': list(budgets),
        }

        return Response(response_data)
