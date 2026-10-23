from django.shortcuts import render, redirect, get_object_or_404
from.models import Movie
from .forms import MovieForm
import requests

def home(request):
    response= requests.get('https://omdbapi.com/?apikey=38b4b85b&s=Batman&type=movie')
    results_json = response.json()
    movies = results_json['Search']
    context = {
        "movies": movies
    }
    return render(request, 'index.html', context)

def home2(request):
    movies= Movie.objects.all()
    return render(request, 'home.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home2')
    else:
        form = MovieForm()
    return render(request, 'movie_form.html', {'form': form, 'action': 'Register'})

def movie_update(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('home2')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movie_form.html', {'form': form, 'action': 'Update'})

def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('home2')
    return render(request, 'movie_confirm_delete.html', {'movie': movie})
