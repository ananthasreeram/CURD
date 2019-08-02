from django.shortcuts import render
from .forms import MovieForm
from .models import MovieData
from django.http.response import HttpResponse

def home_view(request):
    return render(request,'movie_home.html')

def add_movie_view(request):
    if request.method == "POST":
        form=MovieForm(request.POST)
        if form.is_valid():
            movie_name=request.POST.get('movie_name','')
            hero_name=request.POST.get('hero_name','')
            heroine_name=request.POST.get('heroine_name','')
            director_name=request.POST.get('director_name','')
            rating=request.POST.get('rating','')
            release_date=request.POST.get('release_date','')
            budget=request.POST.get('budget','')
            Data=MovieData(
                movie_name=movie_name,
                hero_name=hero_name,
                heroine_name=heroine_name,
                director_name=director_name,
                rating=rating,
                release_date=release_date,
                budget=budget,
            )
            Data.save()
            form=MovieForm()
            return render(request,'add_movie.html',{'form':form})
    else:
        form = MovieForm()
        return render(request, 'add_movie.html', {'form': form})

def movie_list_view(request):
    movieslist = MovieData.objects.all()
    return render(request,'list_movie.html',{'movieslist':movieslist})
