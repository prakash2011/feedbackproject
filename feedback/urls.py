"""
URL configuration for feedback project.

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
from django.urls import path,include
from home.views import *

urlpatterns = [
    path('',index,name="index"),
    path('feedback/<id>/',Customer_feedback,name="customer_feedback"),
    path('thank-you/',thank_you,name="thank-you"),
    path('register/',register,name='register'),
    path('about/',about,name='about'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
