from django.shortcuts import render
from django.views import generic

from .models import Doctor


class DoctorCreate(generic.CreateView):
    model = Doctor
    fields = "__all__"
    success_url = "list"


class DoctorList(generic.ListView):
    model = Doctor
