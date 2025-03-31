from django.contrib.auth.backends import ModelBackend
from all_admin.models import AllAdmin

class CustomAuthenticationBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            user = AllAdmin.objects.get(mail=username)
            if user.check_password(password):
                return user
        except AllAdmin.DoesNotExist:
            return None
        return None

    def get_user(self, user_id):
        try:
            return AllAdmin.objects.get(pk=user_id)
        except AllAdmin.DoesNotExist:
            return None