from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from packages.views import base, packages, packagesJapan, packagesChina, featurePackages
from attractions.views import attractions, attractionsChina, attractionsJapan
from bookings.views import checkout, dashboard, removeBooking
from accounts.views import signup, login
from django.conf.urls.static import static

urlpatterns = [
    path('', featurePackages, name="base"),
    path('admin/', admin.site.urls),
    path('packages/', packages, name="packages"),
    path('packages/Japan', packagesJapan, name="packagesJapan"),
    path('packages/China', packagesChina, name="packagesChina"),
    path('signup/', signup, name="signup"),
    path('', include('django.contrib.auth.urls')),
    path('attractions/', attractions, name="attractions"),
    path('attractions/China', attractionsChina, name="attractionsChina"),
    path('attractions/Japan', attractionsJapan, name="attractionsJapan"),
    path('checkout/<int:package_id>', checkout, name="checkout"),
    path('dashboard/', dashboard, name="dashboard"),
    path('dashboard/remove/<int:booking_id>', removeBooking, name="removeBooking"),
    
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
