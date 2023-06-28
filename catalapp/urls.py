from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
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
    path('subscription/<int:software_id>/', views.subscription_view, name='subscription'),#done

    path("profile/", views.profile_view, name="profile"),#??
#     path('subscription/create/', views.create_subscription, name='create_subscription'),
    path('success/', views.success_view, name='success'),
    path('stripe_webhook/', csrf_exempt(views.webhook), name='stripe_webhook'),
    path('payment/redirect/<int:software_id>/', views.redirect_to_payment, name='redirect_to_payment'),
#     path('payment/', views.payment_view, name='payment'),
]
#1.there should be a way when user completes the transaction via stripe,it should reflect back to 
#the database that as a record that this user has made purchase for this software and 
#2.user should be redirected back to the
#user dashboard where he has access to the application for download 
#3.user dashboard creation needs to be done.