from django.urls import path

from . import views


urlpatterns = [
    path('users/', views.users_view, name='users'),
    path('user/<int:user_id>', views.user_view, name='user')
]