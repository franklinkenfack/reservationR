import json
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.db import transaction
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import AllAdmin
from agence.models import Agency
from django.contrib.auth.hashers import make_password
from sys_admin.models import SysAdmin
from all_admin.models import  AllAdmin
from authorisation.models import  Authorisation
from utils.utils import generator_password
from utils.error_page import error_page
from django.http import JsonResponse  # Pour renvoyer des erreurs JSON à partir de la vue
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

User = get_user_model()

def login_view(request):
    return render(request, 'login-page.html')

@login_required
def dashboard_superadmin(request):
    return render(request, 'superadmin/dashboard-page.html')


@login_required
def dashboard_line(request):
    return render(request, 'line/dashboard.html')

@login_required
def dashboard_driver(request):
    return render(request, 'driver/dashboard.html')

@login_required
def dashboard_vehicle(request):
    return render(request, 'vehicle/dashboard.html')

@login_required
def dashboard_trip(request):
    return render(request, 'trip/dashboard.html')

@login_required
def dashboard_agency(request):
    return render(request, 'agency/dashboard.html')

@login_required
def password_recovery(request):
    return render(request, 'password-recovery-page.html')

@login_required
def password_link_notify(request):
    return render(request, 'notify/send-link-password.html')


@login_required
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

    return render(request, 'superadmin/add-admin-page.html', {"agencies": json.dumps(agency_list)})


@login_required
@transaction.atomic
def save_admin(request):
    if request.method == 'POST':
        # Récupération des données du formulaire
        admin_name = request.POST.get('admin_name').strip()
        mail = request.POST.get('mail').strip()
        country = request.POST.get('country').strip()
        city = request.POST.get('city').strip()
        localite = request.POST.get('localite').strip()
        country_code = request.POST.get('country_code').strip()
        tel_number = request.POST.get('tel_number').strip()
        agency_ids = request.POST.getlist('authorised_agencies')  # Liste des agences sélectionnées
        
        # Vérification que tous les champs requis sont présents et non vides
        if not admin_name or not mail or not country or not city or not localite or not country_code or not tel_number or not agency_ids:
            return JsonResponse({'error': 'Tous les champs doivent être remplis.'}, status=400)

        # Vérification de l'existence de l'admin_name ou de l'email dans la base de données
        if AllAdmin.objects.filter(admin_name=admin_name).exists():
            return JsonResponse({'error': 'Le nom d\'administrateur existe deja.'}, status=400)
        
        if AllAdmin.objects.filter(mail=mail).exists():
            return JsonResponse({'error': 'E-mail a déjà associé à un administrateur.'}, status=400)
        
        # Création de l'admin dans AllAdmin
        all_admin = AllAdmin.objects.create(
            admin_name=admin_name,
            country=country,
            city=city,
            localite=localite,
            mail=mail,
            country_calling_code=country_code,
            tel_number=tel_number,
        )

        # Création du SysAdmin lié à cet AllAdmin
        sys_admin = SysAdmin.objects.create(all_admin=all_admin)

        # Ajout des autorisations dans la table `Authorisation`
        try:
            agency_ids = [int(a) for a in agency_ids if a.isdigit()]  # Conversion en int

            agencies = Agency.objects.filter(agency_id__in=agency_ids)
            
            for agency in agencies:
                auth = Authorisation.objects.create(sys_admin=sys_admin, agency=agency)
                print(f"Autorisation créée : {auth}")

        except Exception as e:
            return JsonResponse({'error': 'Erreur lors de la creation d\'une authorisation'}, status=400)
        
        # Retourner un JSON avec l'ID de l'utilisateur pour la redirection
        return JsonResponse({"admin_id": all_admin.admin_id}, status=200)
        #return render(request, 'generate-password.html', context)

    return render(request, 'superadmin/dashboard-page.html')

@login_required
def generate_password(request, id):
    admin = get_object_or_404(AllAdmin, admin_id=id)

    # Vérifier si un mot de passe est déjà généré, sinon en créer un nouveau
    if not admin.password:  # Si aucun mot de passe n'est défini
        password = generator_password()  # Générer un nouveau mot de passe
        admin.password = make_password(password)  # Hacher le mot de passe et le sauvegarder
        admin.save()
    else:
        return HttpResponse(error_page, content_type="text/html")

    context = {
        "admin_name": admin.admin_name,
        "password": password,  # Passer le mot de passe en clair au template
    }
    return render(request, 'generate-password.html', context)

from django.contrib.auth import authenticate, login
from django.http import JsonResponse



def connexion(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        
        if not email or not password:
            return JsonResponse({"success": False, "error": "Tous les champs sont obligatoires."})

        try:
            # Vérification directe de l'utilisateur
            user = AllAdmin.objects.get(mail=email)
            if user.check_password(password) and user.is_active:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Mot de passe incorrect."})
                
        except AllAdmin.DoesNotExist:
            return JsonResponse({"success": False, "error": "Aucun utilisateur avec cet email."})
    
    return JsonResponse({"success": False, "error": "Méthode non autorisée."})

@login_required
def deconnexion(request):
    logout(request)
    request.session.flush()  # Vide complètement la session
    return redirect('login_view')  # Ajoute return pour effectuer la redirection
