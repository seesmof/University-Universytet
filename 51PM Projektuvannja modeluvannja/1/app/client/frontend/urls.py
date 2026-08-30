from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    # path("list", views.measurements_list, name="list"),
    path("list", views.ListMeasurements.as_view(), name="list"),
    # path("list/<int:id>", views.measurement_details, name="details"),
    path("list/<pk>", views.MeasurementDetails.as_view(), name="details"),
    # path("create", views.create_measurement, name="create"),
    path("create", views.CreateMeasurement.as_view(), name="create"),
]
