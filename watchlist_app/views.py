""" from django.shortcuts import render
from watchlist_app.models import Movie
from django.http import HttpResponse , JsonResponse

def movie_list(request):
    movies = Movie.objects.all()
    data = {
        'movies':list(movies.values())
    }
    return JsonResponse(data)
    
def movie_details(request, pk):
    movie = Movie.objects.get(pk=pk)
    data = {
        'pk':pk,  # Add primary key to the response data for future reference.
        'title':movie.title,
        'description':movie.description,
        'active':movie.active,
    }
    return JsonResponse(data) """