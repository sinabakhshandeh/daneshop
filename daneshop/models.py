from django.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    class Status(models.TextChoices):
        PUBLISHED = "published", _("PUBLISHED")
        PENDING = "pending", _("PENDING")
        ARCHIVE = "archive", _("ARCHIVE")
        TRASH = "trash", _("TRASH")

    status = models.CharField(
        max_length=25,
        choices=Status.choices,
        default=Status.PENDING,
        help_text=_("Status"),
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
