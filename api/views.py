# from django.shortcuts import render # no lo usaremos
from rest_framework import viewsets
from .serializer import ProgramerSerializer
from .models import Programmer

# Create your views here.


class ProgramerViewSet(viewsets.ModelViewSet):
    # lista de elementos que se accede del ORM (Object Relational MApping) jango
    queryset = Programmer.objects.all()
    
    # se le entrega la clase que codificamos
    serializer_class = ProgramerSerializer
