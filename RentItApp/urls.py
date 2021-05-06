from django.urls import path
from .import views
urlpatterns= [
    path('home', views.home, name = 'homescreen'),
    path('login', views.login, name = 'login screen'),
    path('signup', views.registeruser, name = 'signup'),
    path('forgotpassword', views.forgotpassword, name = 'forgot password'),
    path('help', views.help, name= 'help'),
    path('help2', views.help2, name= 'help2'),
    path('contact', views.contact, name= 'contact'),

]
