from rest_framework import serializers
from .models import TodoApp

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoApp
        fields = '__all__'