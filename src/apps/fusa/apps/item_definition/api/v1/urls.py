from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('item', views.ItemView, basename='item')
router.register('function', views.FunctionView, basename='function')

app_name = 'fusa'

urlpatterns = [
    path('fusa/', include(router.urls)),
    path('fusa/item/<int:pk>/function', views.FunctionCreate.as_view(), name='function-create')

]