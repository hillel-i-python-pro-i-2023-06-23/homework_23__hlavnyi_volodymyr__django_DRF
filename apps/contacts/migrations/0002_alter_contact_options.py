# Generated by Django 4.2.6 on 2023-10-28 13:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="contact",
            options={"ordering": ["id"]},
        ),
    ]
