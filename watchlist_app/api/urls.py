from django.urls import path,include
from watchlist_app.api import views

urlpatterns = [
    path('list/',views.WatchListAV.as_view()),
    path('<int:pk>/',views.WatchDetailAV.as_view()),
    path('stream/',views.StreamPlatformAV.as_view()),
    path('stream/<int:pk>/',views.StreamPlatformDetailAV.as_view())
]