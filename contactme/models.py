from django.db import models
from django.urls import reverse


# Create your models here.
class ContactMe(models.Model):
    """Model definition for Contacme."""

    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone_number = models.CharField(max_length=25)
    message = models.TextField()

    class Meta:
        """Meta definition for ContacMe."""

        verbose_name = "ContactMe"
        verbose_name_plural = "ContactMes"

    def __str__(self):
        return self.name

    def get_absolute_url(self):

        return reverse("contactme-list")
