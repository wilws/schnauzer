
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import generics
from .models import Bond
from .serializers import BondSerializer
# Create your views here.



class BondListCreateAPIView(generics.ListCreateAPIView):
 
    queryset = Bond.objects.all()
    serializer_class = BondSerializer
    # allow_staff_view = True
