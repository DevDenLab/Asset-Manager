from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy

app_name = "catalapp"
urlpatterns = [
    path("home/", views.home, name="home"),
    path(
        "home/detail/<int:software_id>/", views.softwaredetails, name="softwaredetails"
    ),
    path("plugins/", views.plugins, name="plugins"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("api/search/", views.search_api, name="search_api"),
    path("user_auth/", views.authenticate, name="auth"),
    path("login/", views.login_view, name="login"),
    path("register/", views.register_view, name="register"),
    path(
        "logout/",
        auth_views.LogoutView.as_view(next_page=reverse_lazy("catalapp:home")),
        name="logout",
    ),
    path("profile/", views.profile_view, name="profile"),
]
