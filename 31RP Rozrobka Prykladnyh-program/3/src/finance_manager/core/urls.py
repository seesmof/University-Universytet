from django.urls import path
from .views import login_view, user_dashboard_view

urlpatterns = [
    path('login/', login_view, name='login'),
    path('', login_view, name='home'),
    path('user/<int:user_id>/', user_dashboard_view, name='user_dashboard'),
]