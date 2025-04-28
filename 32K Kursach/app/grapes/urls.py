from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('bunches/<int:id>',views.bunches,name='bunch')
]
