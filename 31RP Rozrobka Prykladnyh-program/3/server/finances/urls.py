from django.urls import path

from server.finances import views


urlpatterns=[
    path('',views.index,name='Home')
]