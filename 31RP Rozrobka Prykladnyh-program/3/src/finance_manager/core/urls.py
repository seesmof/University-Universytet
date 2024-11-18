from django.urls import path
from .views import login_view, user_dashboard

urlpatterns = [
    path('login/', login_view, name='login'),
    path('user_dashboard/<int:user_id>/', user_dashboard, name='user_dashboard'),
    path('', login_view, name='login'),
]