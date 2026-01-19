from django.urls import path

from backend.frontend import views

urlpatterns = [
    path("store", views.StoreForm.as_view(), name="store"),
    path("signup", views.SignUpForm.as_view(), name="signup"),
    path("login", views.LoginForm.as_view(), name="login"),
]
