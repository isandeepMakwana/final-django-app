from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('login', views.user_login, name='login'),
    path('register', views.register, name='register'),
    path('special', views.special, name='special'),
    path('logout', views.user_logout, name='logout'),
    path('payment', views.payment, name='payment'),
    path('special', views.home, name='special'),
    ]
 