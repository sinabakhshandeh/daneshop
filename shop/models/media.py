import os
import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _

from daneshop.models import BaseModel


def author_title_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    product = instance.product
    slug = slugify(product.title)
    path = f"product_{product.id}/{slug}"
    unique_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(path, unique_filename)


class ProductMedia(BaseModel):
    class FileType(models.TextChoices):
        IMAGE = "image", _("IMAGE")
        VIDEO = "video", _("VIDEO")

    file_type = models.CharField(
        max_length=25,
        choices=FileType.choices,
        default=FileType.IMAGE,
        help_text=_("File Type"),
    )

    file = models.FileField(
        upload_to=author_title_upload_path,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        "Product",
        on_delete=models.CASCADE,
        related_name="medias",
    )

    def __str__(self):
        return f"{self.file_type}: {os.path.basename(self.media.name)}"
