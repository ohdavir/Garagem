from rest_framework.serializers import ModelSerializer

from .models import Acessorio

class AcessorioViewSet(viewsets.ModelViewSet):
    queryset = Acessorio.objects.all()
    serializer_class = AcessorioSerializer