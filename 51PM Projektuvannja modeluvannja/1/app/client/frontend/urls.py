from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("list", views.measurements_list, name="list"),
    path("list/<int:id>", views.measurement_details, name="details"),
    path("create", views.create_measurement, name="create"),
]
