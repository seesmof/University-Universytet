from django.urls import path

from . import views

app_name = 'grapes'
urlpatterns = [
    path('',views.index,name='index'),
    path('bunches/<int:id>',views.bunches,name='bunch')
]
