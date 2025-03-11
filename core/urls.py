from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.home.urls')),
    path('admin/', admin.site.urls),
    path('auth/', include('apps.accounts.urls')),
    path('support/', include('apps.support.urls')),
    path('dashboard/', include('apps.dashboard.urls')),
]
