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
    context = {
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices,
    }
    return render(request, 'listings/search.html', context)
