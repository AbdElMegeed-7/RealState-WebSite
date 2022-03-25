from django.shortcuts import get_object_or_404, render
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger
from .models import Listings
from .choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listings.objects.order_by(
        '-list_date').filter(is_published=True)
    paginator = Paginator(listings, 4)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        # 'listings': listings,
        'listings': paged_listings,
    }
    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listings, pk=listing_id)

    context = {
        'listing': listing,
    }
    return render(request, 'listings/listing.html', context)


def search(request):
    queryset_list = Listings.objects.order_by(
        '-list_date')

    # Search by keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)
    # Search by city
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__iexact=city)
    # Search by state
    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            queryset_list = queryset_list.filter(state__iexact=state)
    # Search by bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)
    # Search by Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)

    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
        'listings': queryset_list,
    }
    return render(request, 'listings/search.html', context)
