from django.urls import path, include
from landing import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
]
