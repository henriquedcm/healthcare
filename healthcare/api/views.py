from rest_framework import permissions, viewsets

from healthcare.api.serializers import (
    PatientSerializer,
)
from healthcare.api.models import Patient


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by("name")
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]
