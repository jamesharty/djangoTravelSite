from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger ,Paginator
from django.shortcuts import render, redirect, get_object_or_404
from packages.models import Package
from bookings.models import Booking
from accounts.models import Profile
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.
def checkout(request, package_id):

    package = get_object_or_404(Package, pk=package_id) 

    context ={
       'package':package
   }

    return render(request, 'pages/checkout.html', context)


def dashboard(request):
    if request.method =='POST':
        customerID= request.POST['customerID']
        packageName = request.POST['packageName']
        price = request.POST['price']
        startDate = request.POST['startDate']
        endDate = request.POST['endDate']
 
        newBooking = Booking(customerID = customerID, packageName = packageName, price=price,startDate=startDate,endDate=endDate)
        newBooking.save() 

        booking = Booking.objects.order_by('-packageName').filter(customerID=request.user.profile.id)

        context = {
                'bookings' : booking
            }


        send_mail(
            'Holiday Booking',
            'Thanks for booking your holiday with us!.\n'
            'Package Name: ' + packageName +'\n'
            'Package Price : €' + price +'\n',
            'simpleTravel@simple.com',
            [request.user.email],
            fail_silently=False,
            )
        return render(request, 'pages/dashboard.html',context)

    else:
        booking = Booking.objects.order_by('-packageName').filter(customerID=request.user.profile.id)

        context = {
                'bookings' : booking
            }
        return render(request, 'pages/dashboard.html',context)


def removeBooking(request, booking_id):

    Booking.objects.filter(id=booking_id).delete()

    booking = Booking.objects.order_by('-packageName').filter(customerID=request.user.profile.id)

    context = {
                'bookings' : booking
            }
    return render(request, 'pages/dashboard.html',context)
    
