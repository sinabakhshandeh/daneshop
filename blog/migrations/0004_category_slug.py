# Generated by Django 4.2 on 2024-02-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_category_created_at_category_status_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default="", max_length=200, unique=True),
        ),
    ]
