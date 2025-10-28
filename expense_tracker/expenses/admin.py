from django.contrib import admin
from .models import Category, Expense

admin.site.register(Category)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'amount', 'date')
    list_filter = ('category', 'date')
    search_fields = ('title', 'note')
