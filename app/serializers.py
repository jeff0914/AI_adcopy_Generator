from rest_framework import serializers
from .models import AdCopy

class AdCopySerializer(serializers.ModelSerializer):
    class Meta:
        model = AdCopy
        fields = ['uuid', 'user_input', 'generated_text', 'timestamp']
