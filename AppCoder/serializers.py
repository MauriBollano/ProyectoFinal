from rest_framework import serializers
from .models import *
from .views import *

class RecetasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recetas
        fields = '__all__'