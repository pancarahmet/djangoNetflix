from django.shortcuts import render
from .models import *
from django.db.models import Q

# Create your views here.


def browse_index(request):
    filmler=Movies.objects.all()
    search_movie=""
    if request.GET.get("search_movie"):
        search_movie=request.GET.get("search_movie")
        filmler=filmler.filter(
                Q(name__icontains=search_movie)
        )
    context={
        "filmler":filmler,
        "search":search_movie
    }
    return render(request,"browse-index.html", context)