from django.db import models
from django.conf import settings
from categories.models import Category
from django.utils import timezone

class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True, related_name='expenses')
    description = models.TextField(blank=True)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.description}: {self.amount} on {self.date}"
