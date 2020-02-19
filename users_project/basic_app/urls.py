from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views
from django.conf.urls import url

app_name = 'basic_app'


urlpatterns = [
    path('register/' , views.register , name = 'register'),
    path('user_login/', views.user_login , name = 'user_login')
]
