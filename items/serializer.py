from rest_framework import serializers
from .models import PersonaPDP

class PersonaPDP_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PersonaPDP
        fields = '__all__'