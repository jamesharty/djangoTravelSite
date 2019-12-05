from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger ,Paginator
from django.shortcuts import render, redirect, get_object_or_404
from .models import Package
from attractions.models import Attraction
from bookings.models import Booking
from accounts.models import Profile

def base(request):

    return render(request,'pages/index.html')

 
def featurePackages(request):

    packages = Package.objects.order_by('-type')
    paginator = Paginator(packages,3)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    context = {
        'packages': paged_packages
    }

    return render(request, 'pages/index.html',context)

def packages(request):

    packages = Package.objects.order_by('price')
    paginator = Paginator(packages,6)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    context = {
        'packages': paged_packages
    }

    return render(request, 'pages/packages.html',context)


def packagesJapan(request):

    packages = Package.objects.order_by('price').filter(country="Japan")
    paginator = Paginator(packages,6)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    context = {
        'packages': paged_packages
    }

    return render(request, 'pages/packages.html',context)

def packagesChina(request):

    packages = Package.objects.order_by('price').filter(country="China")
    paginator = Paginator(packages,6)
    page = request.GET.get('page')
    paged_packages = paginator.get_page(page)

    context = {
        'packages': paged_packages
    }

    return render(request, 'pages/packages.html',context)



