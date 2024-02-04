from rest_framework import serializers
from .models import Budget
from categories.models import Category
from categories.serializers import CategorySerializer

class BudgetSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'category_id', 'amount']
        read_only_fields = ('user',) 

    def validate_amount(self, value):
        """Ensure the budget amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Budget amount must be greater than zero.")
        return value
