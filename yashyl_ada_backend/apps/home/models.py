from django.db import models
from django.utils.translation import gettext_lazy as _


class ContactUs(models.Model):
    email = models.EmailField()
    company = models.CharField(max_length=250, blank=True, null=True)
    phone = models.CharField(max_length=50)
    text = models.TextField(max_length=500)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = _('Contact us mails')
        verbose_name = _('Contact us mail')
