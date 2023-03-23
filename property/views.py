from django.shortcuts import render

from property.models import Flat
from property.models import Claim


def format_price(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def show_claim(request):
    username = request.GET.get('username')
    flat = (request.GET.get('town'), request.GET.get('address'))
    claim_text = request.GET.get('claim_text')

    claim = Claim.onjects.all()
    if username:
        claim = claim.filter(username=username)
    if flat:
        claim = claim.filter(flat=flat)


def show_flats(request):
    town = request.GET.get('town')
    min_price = format_price(request.GET.get('min_price'))
    max_price = format_price(request.GET.get('max_price'))
    liked_by = request.GET.get('liked_by')
    new_building = request.GET.get('new_building') == '1'

    flats = Flat.objects.all()
    if town:
        flats = flats.filter(town=town)
    if min_price:
        flats = flats.filter(price__gt=min_price)
    if max_price:
        flats = flats.filter(price__lt=max_price)
    if new_building:
        flats = flats.filter(new_building=True)

    towns = Flat.objects.values_list(
        'town', flat=True).distinct().order_by('town')

    return render(request, 'flats_list.html', {
        'flats': flats[:10],
        'towns': towns,
        'active_town': town,
        'max_price': max_price,
        'min_price': min_price,
        'new_building': new_building})
