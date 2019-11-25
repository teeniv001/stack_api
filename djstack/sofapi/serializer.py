from rest_framework import serializers
from .models import questions

class questionserializer(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = ('__all__')
