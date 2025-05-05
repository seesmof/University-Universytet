from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'grapes'
urlpatterns = [
    path('',views.index,name='index'),
    path('bunch/<int:id>',views.bunch,name='bunch'),
    path('new_bunch',views.new_bunch,name='new_bunch'),
    path('profile',views.profile,name='profile'),
]