from django.urls import path, include
from landing import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('services/', views.AboutView.as_view(), name='services_page'),
    path('equipments/', views.AboutView.as_view(), name='equipments_page'),
    path('contact/', views.AboutView.as_view(), name='contact_page'),
    path('quote/', views.AboutView.as_view(), name='quote_page'),
]
