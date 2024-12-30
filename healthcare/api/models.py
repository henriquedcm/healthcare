from django.db import models
from django.utils.translation import gettext_lazy as _


class HumanNameUse(models.TextChoices):
    USUAL = "usual", _("Usual")
    OFFICIAL = "official", _("Official")
    TEMP = "temp", _("Temp")
    NICKNAME = "nickname", _("Nickname")
    ANONYMOUS = "anonymous", _("Anonymous")
    OLD = "old", _("Old")
    MAIDEN = "maiden", _("Name changed for Marriage")


class ContactPointSystem(models.TextChoices):
    PHONE = "phone", _("Phone")
    FAX = "fax", _("Fax")
    EMAIL = "email", _("Email")
    PAGER = "pager", _("Pager")
    URL = "url", _("URL")
    SMS = "sms", _("SMS")
    OTHER = "other", "Other"


class ContactPointUse(models.TextChoices):
    HOME = "home", _("Home")
    WORK = "work", _("Work")
    TEMP = "temp", _("Temp")
    OLD = "old", _("Old")
    MOBILE = "mobile", _("Mobile")


class AddressUse(models.TextChoices):
    HOME = "home", _("Home")
    WORK = "work", _("Work")
    TEMP = "temp", _("Temp")
    OLD = "old", _("Old")
    BILLING = "billing", _("Billing")


class AddressType(models.TextChoices):
    POSTAL = "postal", _("Postal")
    PHYSICAL = "physical", _("Physical")
    BOTH = "both", _("Both")


class Gender(models.TextChoices):
    MALE = "male", _("Male")
    FEMALE = "female", _("Female")
    OTHER = "other", _("Other")
    UNKNOWN = "unknown", _("Unknown")


class HumanName(models.Model):
    use = models.CharField(choices=HumanNameUse.choices, max_length=50)
    text = models.CharField(blank=True, max_length=255)
    family = models.CharField(blank=True, max_length=150)
    given = models.JSONField(default=list, blank=True)
    prefix = models.JSONField(default=list, blank=True)
    suffix = models.JSONField(default=list, blank=True)
    period = models.JSONField(default=dict, blank=True)


class ContactPoint(models.Model):
    system = models.CharField(max_length=20, choices=ContactPointSystem.choices)
    value = models.CharField(max_length=255, blank=True)
    use = models.CharField(max_length=20, choices=ContactPointUse.choices)
    rank = models.PositiveIntegerField(null=True)
    period = models.JSONField(default=dict, blank=True)


class Address(models.Model):
    use = models.CharField(choices=AddressUse.choices, max_length=50)
    type = models.CharField(choices=AddressType.choices, max_length=50)
    text = models.TextField(blank=True)
    line = models.JSONField(default=list)
    city = models.CharField(max_length=150, blank=True)
    district = models.CharField(max_length=150, blank=True)
    state = models.CharField(max_length=150, blank=True)
    postal_code = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=150, blank=True)
    period = models.JSONField(default=dict, blank=True)


class Patient(models.Model):
    """https://www.hl7.org/fhir/patient.html"""

    # identifier = models.JSONField(default=list, blank=True)
    active = models.BooleanField(default=True)
    name = models.ManyToManyField(HumanName, related_name="patients")
    telecom = models.ManyToManyField(ContactPoint, related_name="patients")
    gender = models.CharField(
        choices=Gender.choices, default=Gender.UNKNOWN, max_length=50
    )
    birth_date = models.DateField(blank=True)
    deceased_boolean = models.BooleanField(default=False)
    deceased_datetime = models.DateTimeField(blank=True)
    address = models.ManyToManyField(Address, related_name="patients")
    marital_status = models.JSONField(default=dict)
    multiple_birth_boolean = models.BooleanField(default=False)
    multiple_birth_integer = models.IntegerField(null=True)
    photo = models.JSONField(default=list)
    contact = models.JSONField(default=list)
    communication = models.JSONField(default=list)
    general_practitioner = models.JSONField(default=list)
    managing_organization = models.JSONField(default=dict)
    link = models.JSONField(default=list)
