from rest_framework import serializers
from .models import Expense
from categories.models import Category
from categories.serializers import CategorySerializer
from django.utils import timezone

class ExpenseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all(), source='category', write_only=True)

    class Meta:
        model = Expense
        fields = ['id', 'user', 'amount', 'category', 'category_id', 'description', 'date']
        read_only_fields = ('user',)

    def validate_amount(self, value):
        """Ensure the expense amount is positive."""
        if value <= 0:
            raise serializers.ValidationError("Expense amount must be greater than zero.")
        return value

    def validate_date(self, value):
        """Ensure the expense date is not in the future."""
        if value > timezone.now().date():
            raise serializers.ValidationError("Expense date cannot be in the future.")
        return value

    def validate_description(self, value):
        """Optional: Validate description for a minimum length or other criteria."""
        if len(value) < 6:
            raise serializers.ValidationError("Description must be at least 6 characters long.")
        return value