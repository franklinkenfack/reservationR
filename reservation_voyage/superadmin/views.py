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

# Envoi de mail
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.conf import settings

from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.views import PasswordResetView,PasswordResetConfirmView
from django.core.mail import send_mail, EmailMessage
from django.contrib import messages
from .tokens import account_activation_token  # Assurez-vous que le token est bien importé


User = get_user_model()

def login_view(request):
    return render(request, 'login-page.html')

@login_required
def dashboard_superadmin(request):
    print("code")
    print(request.user)  
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

        # Utilisation du backend personnalisé
        user = authenticate(request, username=email, password=password)
        
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({"success": True})
            else:
                return JsonResponse({"success": False, "error": "Ce compte est désactivé."})
        else:
            return JsonResponse({"success": False, "error": "Email ou mot de passe incorrect."})
    
    return JsonResponse({"success": False, "error": "Méthode non autorisée."})

@login_required
def deconnexion(request):
    logout(request)
    request.session.flush()  # Vide complètement la session
    return redirect('login_view')  # Ajoute return pour effectuer la redirection



def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = AllAdmin.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, AllAdmin.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()

        messages.success(request, 'Merci pour la confirmation de votre email. Vous pouvez maintenant vous connecter.')
        return redirect('login_view')  # Vérifiez que 'login_view' est bien défini dans vos URLs
    else:
        messages.error(request, "Le lien d'activation est invalide !")

    return redirect('dashboard_superadmin')


def activateEmail(request, user, to_email):
    context = {
        'user': user,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    }

    email_content = render_to_string('reset-password/acct_active_email.html', context)

    email_subject = 'Activate your account.'
    recipient_list = [to_email]
    from_email = 'allforms@limited.com'

    success = send_mail(
        email_subject,
        '',
        from_email,
        recipient_list,
        html_message=email_content,
        fail_silently=False
    )

    if success > 0:
        messages.success(
            request,
            f"Dear {user}, Please go to your email '{to_email}' inbox and click on "
            f"the received activation link to confirm and complete the registration. Note: Check your spam folder"
        )
    else:
        messages.error(request, f'There was a problem sending email to {to_email}, please make sure your email was spelt correctly.')



def send_custom_password_reset_email(request, user):
    context = {
        'name': user,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': default_token_generator.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http',
        'domain': get_current_site(request).domain,
    }
    subject = 'Password Reset'
    from_email = 'tutomekontchou3@gmail.com'
    to_email = user.email
   
    email_content = render_to_string('reset-password/password_reset_mail.html', context)
    
    msg = EmailMessage(
        subject,
        email_content,
        from_email,
        [to_email],
        alternatives=[(email_content, 'text/html')],
    )
    msg.send()
    
class CustomPasswordResetView(PasswordResetView):
    template_name = 'reset-password/password_reset_form.html'
    email_template_name = 'reset-password/password_reset_mail.html'
    print("toka")
    def form_valid(self, form):
        print("gojo")
        response = super().form_valid(form)
        print("gateau")
        users = list(form.get_users(form.cleaned_data['mail']))
        user = users[0] if users else None

        if user:
            print("go")
            send_custom_password_reset_email(self.request, user)
            print("go go")
            return response
        else:
            print("bouche be")
            messages.error(self.request, 'Activation link is invalid!')


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'reset-password/password_reset_confirm.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uidb64'] = self.kwargs['uidb64']
        context['token'] = self.kwargs['token']
        return context
    
    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Your password has been reset successfully.')
        return super().form_valid(form)