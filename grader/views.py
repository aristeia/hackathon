#from django.shortcuts import render
from django.shortcuts import render, render_to_response
from django.http import Http404
from django.core.context_processors import csrf
from grader.models import *#oster, Band, Musician, Artist, Venue, Genre, Genre_Relation, Artist_Image, Venue_Image
#from django.contrib.auth import authenticate, login, logout
from grader.forms import *



def index(request):
    if request.method == 'POST':
    	form = SubmissionForm(request.POST)
    else:
        form = SubmissionForm()
    return render(request, 'index', {'form'=form})

# Create your views here.
