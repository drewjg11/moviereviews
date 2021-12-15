from django.conf import settings
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('', include('apps.movie.urls')),
    path('', include('apps.fusa.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('api-auth/', include('rest_framework.urls')),
        path('__debug__/', include(debug_toolbar.urls)),
    ]
