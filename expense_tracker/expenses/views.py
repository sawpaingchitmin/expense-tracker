from django.shortcuts import render, redirect, get_object_or_404
from .models import Expense
from .forms import ExpenseForm
from datetime import date
from django.db.models import Sum

def home(request):
    return render(request, 'expenses/home.html')

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    total = expenses.aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'expenses/expense_list.html', {'expenses': expenses, 'total': total})

def expense_detail(request, id):
    expense = get_object_or_404(Expense, id=id)
    return render(request, 'expenses/expense_detail.html', {'expense': expense})

def add_expense(request):
    if request.method == "POST":
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/add_expense.html', {'form': form})