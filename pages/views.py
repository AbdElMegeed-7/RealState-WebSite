from django.shortcuts import render
from listings.models import Listings
from realtors.models import RealTor


def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)[:3]
    context = {
        'listings': listings,
    }
    return render(request, 'pages/index.html', context)


def about(request):
    realtors = RealTor.objects.order_by('-hire_date')
    mvp_realtors = RealTor.objects.all().filter(is_mvp=True)
    
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors,
    }
    return render(request, 'pages/about.html', context)
