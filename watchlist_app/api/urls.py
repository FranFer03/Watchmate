from django.urls import path,include
from watchlist_app.api import views

urlpatterns = [
    path('list/',views.movie_list,name='movie-list'),
    path('<int:pk>/',views.movie_details,name='movie-details')  # Add movie details URL
]