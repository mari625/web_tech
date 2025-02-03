"""
URL configuration for hw_2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

app_name = 'app_1'
urlpatterns = [
    path('', views.home),
    path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('info/', views.info, name='info'),
    path('task_form/', views.task_form, name='task_form'),
    path('task_get/', views.task_get, name='task_get'),
    path('task_model_form/', views.task_model_form, name='task_model_form'),
    path('task_result/', views.task_result, name='task_result'),
    path('table/', views.table, name='table'),
]
