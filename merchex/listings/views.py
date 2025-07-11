from django.http import HttpResponse
from django.shortcuts import render

from listings.models import Band
from listings.models import Listing

def hello(request):
    bands = Band.objects.all()
    listes = Listing.objects.all()

    return render(request, 'listings/hello.html',
                  {'bands': bands, 'listes': listes},
                )
 

def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')

def list(request):
    return HttpResponse('<h1>Liste des articles</h1> <p>voici la liste !</p>')

def contact(request):
    return render(request, 'contacts/contact.html')