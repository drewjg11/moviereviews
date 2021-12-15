from django.urls import include, path
from django.views.generic import TemplateView

urlpatterns = [
    path('api/beta/core/', include('apps.movie.api.v1.urls')),

]