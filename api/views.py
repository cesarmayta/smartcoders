from rest_framework.response import Response
from rest_framework import generics

from .models import Area
from .serializers import AreaSerializer

class AreaApiView(generics.ListCreateAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer
    
class AreaDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Area.objects.all()
    serializer_class = AreaSerializer