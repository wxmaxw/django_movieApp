from django.shortcuts import render
from .models import Category, Movie



# Create your views here.

def home(request):
    data = {
        "Categories" : Category.objects.all(),  #category_list database'den çekmeden önce
        "Movies" : Movie.objects.filter(homepage= True),   #movies_list, #anasayfa parametresi true olanları getirsin diye
    }
    
    return render(request, "index.html", data) # first params must be request, second params must be the relevant html page

def movies(request):
    data = {
        "Categories" : Category.objects.all(),  #category_list database'den çekmeden önce
        "Movies" : Movie.objects.all(),   #movies_list,
    }
    
    return render(request, "movies.html",data) # first params must be request, second params must be the relevant html page

def movie_details(request,id):
    data = {
        "id" : id,
        "movie": Movie.objects.get(id=id) 
    }
    
    return render(request, "details.html", data)



'''
category_list = ['adventure', 'romantic', 'drama', "comedy"]
movies_list = [
    {
        "id":1,
        "movie_name": "Movie 1",
        "explanation": "Movie 1 content",
        "image" : "1.jpeg",
        "homepage": False  # if it is true the film is showed in homepage 
    },
     {
        "id":2,
        "movie_name": "Movie 2",
        "explanation": "Movie 2 content",
        "image" : "2.jpeg",
        "homepage": True
    },
     {
        "id":3,
        "movie_name": "Movie 3",
        "explanation": "Movie 3 content",
        "image" : "3.jpeg",
        "homepage": False
    },
     {
        "id":4,
        "movie_name": "Movie 4",
        "explanation": "Movie 4 content",
        "image" : "4.jpeg",
        "homepage": True
    },
]
'''