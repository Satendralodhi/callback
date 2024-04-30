from rest_framework import serializers
from .models import CALLBACK
class callback_serializers(serializers.ModelSerializer):
    class Meta:
        model= CALLBACK
        fields='__all__'