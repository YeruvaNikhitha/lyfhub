from django.urls import path
from . import views

urlpatterns = [

    path("search/", views.search_donors, name="search_donors"),

    path("emergency/", views.emergency_request, name="emergency"),

    path("dashboard/", views.dashboard, name="dashboard"),

    path("profile/<int:donor_id>/", views.profile, name="profile"),

    path("toggle/<int:donor_id>/", views.toggle_availability, name="toggle"),

]