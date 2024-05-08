from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('consultation/', views.consultation, name='consultation'),
    path('submit_consultation/', views.submit_consultation, name='submit_consultation'),
    path('review/', views.review, name='review'),
    path('services/', views.services, name='services'), 
    path('info/', views.info, name='info'),
    path('contact/', views.contact, name='contact'),
    path('product/', views.product, name='product'),
    path('about-us/', views.about_us, name='about_us'),
    path('inquiry/', views.inquiry, name='inquiry'),
    path('submit_inquiry/', views.submit_inquiry, name='submit_inquiry'),
    
]


