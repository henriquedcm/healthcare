from rest_framework import serializers

from healthcare.api import models
from fhir.resources.patient import Patient
from pydantic.v1.error_wrappers import ValidationError


class PatientSerializer(serializers.HyperlinkedModelSerializer):
    def validate(self, data):
        try:
            Patient.parse_obj(data)
        except ValidationError as err:
            raise serializers.ValidationError(str(err))

        return data

    class Meta:
        model = models.Patient
        fields = "__all__"
