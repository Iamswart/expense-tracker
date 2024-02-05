from rest_framework import serializers
from django.db.models import Sum
from .models import Expense
from budgets.models import Budget
from categories.models import Category
from categories.serializers import CategorySerializer
from django.utils import timezone

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(), source='category', write_only=True
    )

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'category', 'category_id', 'description']
        read_only_fields = ('user',)

    def validate_amount(self, value):
        if value <= 0:
            raise serializers.ValidationError("Expense amount must be greater than zero.")
        return value

    def validate_description(self, value):
        if len(value) < 6:
            raise serializers.ValidationError("Description must be at least 6 characters long.")
        return value

    def validate(self, attrs):
        category = attrs.get('category')
        amount = attrs.get('amount')
        user = self.context['request'].user

        # Adjust the query to either include or exclude the current expense based on if it's an update
        existing_expenses_query = Expense.objects.filter(category=category, user=user)
        if self.instance:
            existing_expenses_query = existing_expenses_query.exclude(id=self.instance.id)
        total_expenses = existing_expenses_query.aggregate(total=Sum('amount'))['total'] or 0
        new_total = total_expenses + amount

        try:
            budget = Budget.objects.get(category=category, user=user)
        except Budget.DoesNotExist:
            budget = None

        if budget and new_total > budget.amount:
            raise serializers.ValidationError({"amount": "This expense exceeds your budget for this category."})

        return attrs
