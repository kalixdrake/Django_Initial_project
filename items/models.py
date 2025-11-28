from django.db import models

# Create your models here.
from django.db import models

class PersonaPDP(models.Model):
    NombrePDP = models.CharField(max_length=200)
    CedulaPDP = models.TextField()
    SerialPDP = models.CharField(max_length=50, default='New')
    
    # This is our bridge to SharePoint
    sharepoint_id = models.CharField(max_length=100, unique=True, null=True, blank=True)

    def __str__(self):
        return self.title