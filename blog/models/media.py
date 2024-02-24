import os
import uuid

from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _


def author_title_upload_path(instance, filename):
    ext = filename.split(".")[-1]
    post = instance.post
    slug = slugify(post.title)
    path = f"user{post.author.id}_{post.author.username}/{slug}"
    unique_filename = f"{uuid.uuid4()}.{ext}"
    return os.path.join(path, unique_filename)


class Media(models.Model):
    class FileType(models.TextChoices):
        IMAGE = "image", _("IMAGE")
        AUDIO = "audio", _("AUDIO")
        VIDEO = "video", _("VIDEO")

    file_type = models.CharField(
        max_length=25,
        choices=FileType.choices,
        default=FileType.IMAGE,
        help_text=_("File Type"),
    )

    media = models.FileField(
        upload_to=author_title_upload_path,
        null=True,
        blank=True,
    )
    post = models.ForeignKey(
        "Post",
        on_delete=models.CASCADE,
        related_name="medias",
    )

    def __str__(self):
        return f"{self.file_type}: {os.path.basename(self.media.name)}"
