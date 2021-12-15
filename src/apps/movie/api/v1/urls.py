from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.movie.api.v1 import views

app_name = 'movie'
#API Endpoints
urlpatterns = format_suffix_patterns([
    path('movies/', views.MovieList.as_view(), name='movie-list'),
    path('movies/<int:pk>/', views.MovieDetail.as_view(), name='movie-detail'),
    path('movies/reviews', views.ReviewList.as_view(), name='review-list'),
    path('movies/review/<int:pk>/', views.ReviewDetail.as_view(), name='review-detail')
])

