from django.urls import include, path
from django.views.generic import TemplateView


urlpatterns = [
    path('api/beta/core/', include('apps.core.api.v1.urls')),
    path('api/beta/docs/swagger/<str:version>/', TemplateView.as_view(
        template_name='core/swagger.html',
    ), name='v3-swagger-ui'),
]
