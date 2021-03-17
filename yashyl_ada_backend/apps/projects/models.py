from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.timezone import now as timezone_now

from sorl.thumbnail import ImageField as SorlImageField


def upload_to(instance, filename):
    now = timezone_now()
    base, extension = os.path.splitext(filename)
    extension = extension.lower()
    return f"project/{now:%Y/%m}/{instance.slug}{extension}"


class Project(models.Model):
    title = models.CharField(unique=True, max_length=250)
    description = models.TextField(max_length=500)
    url = models.URLField()
    image = SorlImageField(_('Image'), upload_to=upload_to, default='img/image_not_found.png')

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')
