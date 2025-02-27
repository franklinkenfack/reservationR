"""
URL configuration for reservation_voyage project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from superadmin.views import dashboard_superadmin
from superadmin.views import dashboard_line
from superadmin.views import dashboard_trip
from superadmin.views import dashboard_driver
from superadmin.views import dashboard_vehicle
from superadmin.views import dashboard_agency
from reservation.views import home
from chauffeur.views import add_driver
from chauffeur.views import save_driver
from superadmin.views import save_admin
from chauffeur.views import save_driver
from agence.views import save_agency
from superadmin.views import add_admin
from agence.views import add_agency

urlpatterns = [
    path('admin/', admin.site.urls),
    path('superadmin/dashboard/', dashboard_superadmin, name='dashboard_superadmin'),
    path('line/dashboard/', dashboard_line, name='dashboard_line'),
    path('trip/dashboard/', dashboard_trip, name='dashboard_trip'),
    path('driver/dashboard/', dashboard_driver, name='dashboard_driver'),
    path('vehicle/dashboard/', dashboard_vehicle, name='dashboard_vehicle'),
    path('agency/dashboard/', dashboard_agency, name='dashboard_agency'),
    path('home/', home, name='home'),
    path('add-driver/', add_driver, name='add_driver'),
    path('save-driver/', save_driver, name='save_driver'),
    path('save-admin/', save_admin, name='save_admin'),
    path('save-agency/', save_agency, name='save_agency'),
    path('add-admin/', add_admin, name='add_admin'),
    path('add-agency/', add_agency, name='add_agency'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)