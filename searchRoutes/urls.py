from django.urls import path
from searchRoutes import views

urlpatterns = [
    path('', views.Flight_Routes_Fun, name='Routes'),
]
