from django.urls import path
from . import views

urlpatterns = [path("list", views.measurements_list, name="list")]
