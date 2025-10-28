from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('list/', views.expense_list, name='expense_list'),
    path('detail/<int:id>/', views.expense_detail, name='expense_detail'),
    path('add/', views.add_expense, name='add_expense'),
]