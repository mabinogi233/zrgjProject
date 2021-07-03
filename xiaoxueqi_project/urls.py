"""xiaoxueqi_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from myDjango.views import run_dev,run_test,run_train,runSQL,get_all

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dev/',run_dev),
    path('test/',run_test),
    path('train/',run_train),
    path('runSQL/',runSQL),
    path('getAll/',get_all),
]
