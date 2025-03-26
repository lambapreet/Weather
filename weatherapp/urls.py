from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('about/', views.about, name="about"),
    path('help/', views.help, name="help"),
    path('delete/<str:city_name>/', views.delete_city, name="delete_city"),  # Added `<str:city_name>`
    path('delete_all/', views.delete_all, name="delete_all"),

]
