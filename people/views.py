from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer, PersonTreeSerializer

# Create your views here.

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    
    @action(detail=False, methods=['get'])
    def tree(self, request):
        """Get the organizational tree"""
        root_nodes = Person.objects.filter(manager__isnull=True)
        serializer = PersonTreeSerializer(root_nodes, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['get'])
    def subtree(self, request, pk=None):
        """Get a subtree starting from a specific person"""
        person = self.get_object()
        serializer = PersonTreeSerializer(person)
        return Response(serializer.data)
