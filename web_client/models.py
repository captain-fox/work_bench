import uuid
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator

phone_regex = RegexValidator(regex=r'^\+?1?\d{9,12}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


class WebUser(User):
    address = models.TextField(blank=True)
    phone_number = models.CharField(validators=[phone_regex], max_length=17, blank=True)
    uploaded_resume = models.FileField(null=True)


class JobOffer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid1, editable=False)
    owner = models.ForeignKey(User)
    start_date = models.DateField(blank=True)
    salary = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=True)
    remote = models.BooleanField(default=False)
    # requirements = models.TextField(blank=True)

