# Generated by Django 4.2.1 on 2023-11-23 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="number1",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("aadhaar", models.BigIntegerField()),
            ],
        ),
        migrations.DeleteModel(name="number",),
    ]
