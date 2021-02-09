from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("user/<int:pk>/", views.profile, name="profile"),
    path("user/<int:pk>/edit", views.edit_profile, name="edit-profile"),
    path("post/<int:pk>/", views.post_detail, name="post-detail"),
    path("sell/", views.sell, name="sell"),
]
