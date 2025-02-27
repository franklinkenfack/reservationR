from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AllAdmin
from agence.models import Agency

def dashboard_superadmin(request):
    return render(request, 'superadmin/dashboard.html')

def dashboard_line(request):
    return render(request, 'line/dashboard.html')

def dashboard_driver(request):
    return render(request, 'driver/dashboard.html')

def dashboard_vehicle(request):
    return render(request, 'vehicle/dashboard.html')

def dashboard_trip(request):
    return render(request, 'trip/dashboard.html')

def dashboard_agency(request):
    return render(request, 'agency/dashboard.html')


def add_admin(request):
    agencies = Agency.objects.filter(state="VISIBLE")  # Récupérer uniquement les agences visibles    
    # Liste avec "Toutes les agences" en premier
    agency_list = [
        {"value": "all", "agency_name": "Toutes les agences"}  # Ajout de l'option par défaut
    ] + [
        {
            "value": agency.agency_id, 
            "agency_name": f"{agency.localite} - {agency.city} - {agency.country}"
        }
        for agency in agencies
    ]

    return render(request, 'superadmin/add-admin.html', {"agencies": agency_list})


def save_admin(request):
    if request.method == "POST":
        admin_name = request.POST.get('admin_name')
        tel_number = request.POST.get('tel_number')
        country = request.POST.get('country')
        city = request.POST.get('city')
        mail = request.POST.get('mail')
        country_code = request.POST.get('country_code')
        agencies_ids = request.POST.getlist('authorised_agencies')  # Liste des agences sélectionnées
        agencies_ids = request.POST.getlist('authorised_agencies')  
        print("IDs des agences sélectionnées:", agencies_ids)

        # Vérification si le numéro de téléphone existe déjà
        if AllAdmin.objects.filter(tel_number=tel_number).exists():
            messages.error(request, "Un administrateur avec ce numéro existe déjà.")
            return render(request, 'admin/add-admin.html', {
                'admin_name': admin_name,
                'tel_number': tel_number,
                'country': country,
                'city': city,
                'mail': mail,
                'country_code': country_code,
                'agencies': Agency.objects.all(),
                'selected_agencies': agencies_ids
            })

        # Création de l'admin
        new_admin = AllAdmin(
            admin_name=admin_name,
            tel_number=tel_number,
            country=country,
            city=city,
            mail=mail,
        )
        new_admin.save()

        # Associer l'admin aux agences sélectionnées
        sys_admin = SysAdmin.objects.create(all_admin=new_admin)
        sys_admin.authorised_agencies.set(agencies_ids)

        messages.success(request, "Administrateur ajouté avec succès.")
        return render(request, 'admin/add-confirmation.html')

    return render(request, 'admin/add-admin.html', {'agencies': Agency.objects.all()})



