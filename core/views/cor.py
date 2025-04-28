from rest_framework.serializers import ModelSerializer

from .models import Cor

class CorViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer