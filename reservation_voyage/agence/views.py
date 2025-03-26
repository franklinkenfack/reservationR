from django.shortcuts import render
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Agency

# Create your views here.
def add_agency(request):
    return render(request, 'agency/add-agency.html')


@transaction.atomic
def save_agency(request):
    if request.method == "POST":
        agency_name = request.POST.get("agency_name")
        country = request.POST.get("country")
        city = request.POST.get("city")
        localite = request.POST.get("localite")
        print(localite)

        # Vérification des champs obligatoires
        if not agency_name or not country or not city or not localite:
             return render(request, 'agency/add-agency.html', {
                'error': "Veuillez remplir tous les champs obligatoires.",
                'title': 'Ajouter une agence',
                'agency_name': agency_name,
                'country': country,
                'city': city,
                'localite': localite,
            })

        # Vérifier si une agence avec le même pays, ville et localité existe déjà
        if Agency.objects.filter(country=country, city=city, localite=localite).exists():
            return render(request, 'agency/add-agency.html', {
                'error': "Cet agence existe deja",
                'title': 'Ajouter une agence',
                'agency_name': agency_name,
                'country': country,
                'city': city,
                'localite': localite,
            })
        # Création et sauvegarde de l'agence
        Agency.objects.create(
            agency_name=agency_name,
            country=country,
            city=city,
            localite=localite,
            state="VISIBLE"  # Définit automatiquement l'état à "VISIBLE"
        )

        # Si l'enregistrement réussit, rediriger vers la page de confirmation
        return render(request, 'notify/add-confirmation.html')

    return redirect("dashboard_agency")  # Redirection en cas d'accès direct à la vue
