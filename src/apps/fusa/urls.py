
from django.urls import path, include

urlpatterns = [
    path('api/beta/core/', include('apps.fusa.apps.item_definition.api.v1.urls')),
]
