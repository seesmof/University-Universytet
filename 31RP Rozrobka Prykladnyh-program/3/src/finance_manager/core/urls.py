from django.urls import path
from .views import login_view, user_dashboard_view, add_transaction_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', login_view, name='home'),
    path('user/<int:user_id>/', user_dashboard_view, name='user_dashboard'),
    path('user/<int:user_id>/add_transaction/', add_transaction_view, name='add_transaction'),
]