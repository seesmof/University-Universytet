from django.urls import path
from . import views

urlpatterns = [
    path("list", views.measurements_list, name="list"),
    path("create", views.create_measurement, name="create"),
]
