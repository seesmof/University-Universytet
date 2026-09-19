from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("task/", views.TaskList.as_view(), name="task_list"),
    path("task/create/", views.TaskCreate.as_view(), name="task_create"),
]
