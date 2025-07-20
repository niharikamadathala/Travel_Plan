from django.shortcuts import render
from .models import ExploreMore


# Create your views here.


def place_list(request):
    places = ExploreMore.objects.all()
    return render(request, 'exploremore/explore_list.html', {'places': places})