from django.shortcuts import render

def add_driver(request):
    return render(request, 'driver/add-driver.html')