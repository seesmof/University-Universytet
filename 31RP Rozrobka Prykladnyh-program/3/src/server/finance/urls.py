from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('client/<int:id>', views.client, name='client'),
    path('deposit/<int:id>', views.deposit, name='deposit'),
    path('withdraw/<int:id>', views.withdraw, name='withdraw'),
    path('edit/<int:id>', views.edit, name='edit'),
]