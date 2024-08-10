"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from home.views import home_page_view
from django.conf import settings
from django.conf.urls.static import static
from home import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),  
    path('about/', include('about.urls')),  # Including the about app's URLs
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', views.HomePageView.as_view(), name='home'),
#     path('projects/', include('projects.urls')),
#     path('blog/', include('blog.urls')),
#     path('contact/', include('contact.urls')),
#     # Add other includes as necessary
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)