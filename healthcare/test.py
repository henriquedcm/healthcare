from fhir.resources.patient import Patient

data = {
    "resourceType": "Patient",
    "id": 1,
    "active": True,
    "name": {"text": "Hello world"},
    "birthDate": "1998-07-16",
    "gender": "male",
    "address": [{"line": ["Rua 5 da Botica"]}],
}

patient = Patient.parse_obj(data)
print(patient)
