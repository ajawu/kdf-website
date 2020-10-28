from django.urls import path
from landing import views

urlpatterns = [
    path('', views.LandingPageView.as_view(), name='landing_page'),
    path('about/', views.AboutView.as_view(), name='about_page'),
    path('services/', views.ServicesView.as_view(), name='services_page'),
    path('equipments/', views.EquipmentPageView.as_view(), name='equipments_page'),
    path('contact/', views.ContactPageView.as_view(), name='contact_page'),
]
