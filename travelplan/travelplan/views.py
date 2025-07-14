from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render


def Home_html(request):
    return render(request, "home.html")
def About_page(request):
    return render(request, "about.html")
def Deals_page(request):
    return render(request, "deals.html")
def Reservation_page(request):
    return render(request, "reservation.html")
