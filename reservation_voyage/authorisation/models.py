from django.db import models
from agence.models import Agency 
from sys_admin.models import SysAdmin 

class Authorisation(models.Model):
    authorisation_id = models.AutoField(primary_key=True)  # ID unique pour chaque autorisation
    sys_admin = models.ForeignKey(SysAdmin, on_delete=models.CASCADE, related_name='authorisations')  
    agency = models.ForeignKey(Agency, on_delete=models.CASCADE, related_name='authorisations')  

    class Meta:
        verbose_name = "Authorisation"
        verbose_name_plural = "Authorisations"
        unique_together = ('sys_admin', 'agency')  # Empêche la duplication des mêmes relations

    def __str__(self):
        return f"Autorisation: {self.sys_admin.all_admin.admin_name} -> {self.agency.agency_name}"
