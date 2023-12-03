from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
    path(r"register", views.register_view, name="register"),
    path(r"login", views.login_view, name="login"),
    path("users", views.Listofname, name='users'),
    path(r"logout/", views.logout_view, name='logout')
]