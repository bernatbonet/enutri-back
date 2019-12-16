"""enutri URL Configuration

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
from django.urls import path, include
from rest_framework.authtoken import views as views_auth_token
from rest_framework_swagger.views import get_swagger_view
from apps.security import urls as urls_security

urlpatterns = [
    path('doc/', get_swagger_view(title='Enutri API')),
    path('api-auth-token/', views_auth_token.obtain_auth_token),
    path('api/', include(urls_security)),
    path('admin/', admin.site.urls),
]