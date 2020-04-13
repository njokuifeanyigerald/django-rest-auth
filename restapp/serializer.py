from rest_framework import serializers
from .models import Rest

class RestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rest
        fields = [
            'job',
            'image',
            'company',
        ]

