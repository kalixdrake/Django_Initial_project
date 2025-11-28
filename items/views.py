from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import PersonaPDP
from .serializer import PersonaPDP_Serializer

class PersonaPDP_ViewSet(viewsets.ModelViewSet):
    # Se le da vista a todos los datos.
    queryset = PersonaPDP.objects.all()

    #Se traduce toda la data desde sharepoint usando el serializador
    serializer_class = PersonaPDP_Serializer