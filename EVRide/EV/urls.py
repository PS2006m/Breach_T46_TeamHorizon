from django.contrib import admin
from django.urls import path
from . import views
urlpatterns=[
    path('',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('otp',views.otp,name='otp'),
    path('home',views.home,name='home'),
    path('vehicle',views.vehicle,name='vehicle'),
    path('book',views.book,name='book'),
    path('reached/',views.reached,name='reached'),
    path('adminui/',views.adminui,name='adminui'),
    path('sm',views.sm,name='sm'),
    path('user_route',views.user_route,name='user_route'),
    path('route_trace',views.route_trace,name='route_trace'),
    path('end_ride',views.end_ride,name='end_ride')
]