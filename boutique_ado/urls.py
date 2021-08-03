"""boutique_ado URL Configuration

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
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), # admin url log in route
    path('accounts/', include('allauth.urls')), # allauth authentication route
    path('', include('home.urls')), # home page url routes
    path('products/', include('products.urls')), # products page url routes
    path('bag/', include('bag.urls')), # bag page url route
    path('checkout/', include('checkout.urls')), # checkout page url route
    path('profile/', include('profiles.urls')),# home page url route
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # renders static files