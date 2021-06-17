from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AppSerializer
from .models import Applicant

# Create your views here.

class TodoView(viewsets.ModelViewSet):
    serializer_class = AppSerializer
    queryset = Applicant.objects.all()