from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Movie, Genre
# Create your views here.

# we create fns that takes requests from the user and emits a response

def index(request):
    return render(request, 'views/index.html')


"""
        read all: Movie.object.all()
        get by id: Movie.objects.get(id=1)
        filter: Movie.objects.filter(in_stock=0)
"""

def catalog(request):
    movies = Movie.objects.all() #read the movies tables
    # titles = ', '.join([m.title for m in movies])
    #HttpResponse(titles)
    return render(request, 'views/catalogtest.html', { 'title' : 'FROM BACKEND', 'movies' : movies } )

def test(request):
    return HttpResponse("This is a test page")

def developer(request):
    return HttpResponse("<h1>Dev: Martin Arredondo</h1>")

def details(request, movie_id):
    try:
        movie = Movie.objects.get(id=movie_id) #read movie
        return render(request, 'views/details.html', { "id": movie_id, "movie":movie })
    except Movie.DoesNotExist:
        raise Http404() 