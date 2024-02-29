# Generated by Django 4.2 on 2024-02-29 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cart", "0002_cart_uuid"),
    ]

    operations = [
        migrations.AddField(
            model_name="cart",
            name="cart_status",
            field=models.CharField(
                choices=[("paid", "PAID"), ("not_paid", "NO_TPAID")],
                default="not_paid",
                help_text="Status",
                max_length=25,
            ),
        ),
    ]