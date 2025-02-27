from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Driver
from django.contrib import messages

def add_driver(request):
    return render(request, 'driver/add-driver.html')


def save_driver(request):
    if request.method == "POST":
        driver_name = request.POST.get('driver_name')
        country = request.POST.get('country')
        city = request.POST.get('city')
        localite = request.POST.get('localite')
        country_code = request.POST.get('country_code')
        phone = request.POST.get('phone')

        # Vérifier si le numéro de téléphone est un nombre
        if not phone.isdigit():
            messages.error(request, "Le numéro de téléphone doit être un nombre valide.")
            return render(request, 'driver/add-driver.html', {
                'title': 'Ajouter un Chauffeur',
                'driver_name': driver_name,
                'country': country,
                'city': city,
                'localite': localite,
                'country_code': country_code,
                'phone': phone
            })
        
        # Vérifier si le numéro de téléphone existe déjà
        if Driver.objects.filter(Tel_number=phone).exists():
            return render(request, 'driver/add-driver.html', {
                'error': 'Un chauffeur avec ce numéro de téléphone existe déjà.',
                'title': 'Ajouter un Chauffeur',
                'driver_name': driver_name,
                'country': country,
                'city': city,
                'localite': localite,
                'country_code': country_code,
                'phone': phone
            })
        
        # Vérifier si le nom existe déjà
        if Driver.objects.filter(driver_name=driver_name).exists():
            return render(request, 'driver/add-driver.html', {
                'error': 'Un chauffeur avec ce nom existe déjà.',
                'title': 'Ajouter un Chauffeur',
                'driver_name': driver_name,
                'country': country,
                'city': city,
                'localite': localite,
                'country_code': country_code,
                'phone': phone
            })

        # Enregistrer le nouveau chauffeur
        driver = Driver(
            driver_name=driver_name,
            country=country,
            city=city,
            localite=localite,
            Tel_number=phone,
            country_calling_code=country_code
        )
        driver.save()

        # Si l'enregistrement réussit, rediriger vers la page de gestion des chauffeurs
        messages.success(request, "Chauffeur ajouté avec succès.")
        return render(request, 'notify/add-confirmation.html')

    # Si ce n'est pas une requête POST, simplement afficher le formulaire
    return render(request, 'driver/add-driver.html', {'title': 'Ajouter un Chauffeur'})