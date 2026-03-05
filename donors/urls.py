from django.urls import path
from . import views

urlpatterns = [

    path('', views.search_donors, name="search_donors"),
    path('dashboard/',views.admin_dashboard,name="dashboard"),

]