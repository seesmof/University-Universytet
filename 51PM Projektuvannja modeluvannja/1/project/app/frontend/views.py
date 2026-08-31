from django.http import HttpRequest
from django.shortcuts import render, redirect
from django.views import generic

from .models import Doctor


def index_view(req: HttpRequest):
    return redirect("list")


class DoctorCreate(generic.CreateView):
    model = Doctor
    fields = "__all__"
    success_url = "/list"


class DoctorList(generic.ListView):
    model = Doctor


class DoctorDelete(generic.DeleteView):
    model = Doctor
    success_url = "/list"
