from django.shortcuts import render
from attractions.models import Attraction
from django.core.paginator import EmptyPage, PageNotAnInteger ,Paginator
# Create your views here.

def attractions(request):
    
    attractions= Attraction.objects.order_by('ranking')
    paginator = Paginator(attractions,6)
    page = request.GET.get('page')
    paged_attractions = paginator.get_page(page)

    context = {
        'attractions': paged_attractions
    }

    return render(request, 'pages/attractions.html',context)


def attractionsChina(request):
    
    attractions= Attraction.objects.order_by('ranking').filter(country="China")
    paginator = Paginator(attractions,6)
    page = request.GET.get('page')
    paged_attractions = paginator.get_page(page)

    context = {
        'attractions': paged_attractions
    }

    return render(request, 'pages/attractions.html',context)

def attractionsJapan(request):
    
    attractions= Attraction.objects.order_by('ranking').filter(country="Japan")
    paginator = Paginator(attractions,6)
    page = request.GET.get('page')
    paged_attractions = paginator.get_page(page)

    context = {
        'attractions': paged_attractions
    }

    return render(request, 'pages/attractions.html',context)