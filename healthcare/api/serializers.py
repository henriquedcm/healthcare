from rest_framework import serializers

from healthcare.api import models


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Address
        fields = "__all__"


class ContactPointSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ContactPoint
        fields = "__all__"


class HumanNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.HumanName
        fields = "__all__"


class PatientSerializer(serializers.ModelSerializer):
    name = HumanNameSerializer(many=True)
    address = AddressSerializer(many=True)
    telecom = ContactPointSerializer(many=True)

    def create(self, validated_data):
        name_data = validated_data.pop("name")
        names = [HumanNameSerializer().create(data) for data in name_data]

        telecom_data = validated_data.pop("telecom")
        telecoms = [ContactPointSerializer().create(data) for data in telecom_data]

        address_data = validated_data.pop("address")
        addresses = [AddressSerializer().create(data) for data in address_data]

        patient = models.Patient.objects.create(**validated_data)

        patient.name.add(*names)
        patient.telecom.add(*telecoms)
        patient.address.add(*addresses)

        return patient

    class Meta:
        model = models.Patient
        fields = "__all__"
