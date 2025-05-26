from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ['id', 'name', 'manager']

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data

class PersonTreeSerializer(serializers.ModelSerializer):
    subordinates = RecursiveField(many=True, read_only=True)
    
    class Meta:
        model = Person
        fields = ['id', 'name', 'subordinates'] 