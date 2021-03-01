
from rest_framework import serializers
from .models import *

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marks
        fields = '__all__'