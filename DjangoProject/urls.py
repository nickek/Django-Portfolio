from django.conf import settings
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('home.urls')),
    path('profile/', include('user_profile.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += path("__debug__/", include("debug_toolbar.urls")),
