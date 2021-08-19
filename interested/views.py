from django.shortcuts import render
from rest_framework import viewsets, permissions

from interested import models
from interested.serializers import InterestedSerializer
# Create your views here.

class InterestedViewSet(viewsets.ModelViewSet):
    queryset = models.Interested.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = InterestedSerializer