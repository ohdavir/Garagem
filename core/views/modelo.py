from rest_framework.serializers import ModelSerializer

from .models import Modelo

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer
