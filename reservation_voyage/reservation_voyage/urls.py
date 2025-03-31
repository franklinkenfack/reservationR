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
from superadmin.views import connexion, password_link_notify, generate_password, deconnexion
# from django.contrib.auth import views as auth_views
from agence.views import save_agency
from superadmin.views import *
from agence.views import add_agency
from django.contrib.auth import views as auth_views

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
    # path('generate-password/', add_driver, name='add_driver'),
    path('save-driver/', save_driver, name='save_driver'),
    path('save-admin/', save_admin, name='save_admin'),
    path('save-agency/', save_agency, name='save_agency'),
    path('add-admin/', add_admin, name='add_admin'),
    path('add-agency/', add_agency, name='add_agency'),
    path('login/', login_view, name='login_view'),
    # path('password-recovery/', password_recovery, name='password_recovery'),
    # path('generate-password/', generate_password, name='generate_password'),
    path('generate-password/<int:id>/', generate_password, name='generate_password'),
    path('password-link-notify/', password_link_notify, name='password_link_notify'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    # path('/', password_link_notify, name='password_link_notify'),
   path('activate/<uidb64>/<token>', activate, name='activate'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('reset/<uidb64>/<token>/', CustomPasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='core/password_reset_done.html'),
          name='password_reset_done'),
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name='core/password_reset_complete.html'),
          name='password_reset_complete'),
 ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)