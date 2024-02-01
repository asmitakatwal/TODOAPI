from rest_framework import serializers
from todo.models import Todo

class TodoModeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields = "__all__"