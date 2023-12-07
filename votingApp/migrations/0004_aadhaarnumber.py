# Generated by Django 4.2.1 on 2023-11-25 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0003_alter_number1_aadhaar"),
    ]

    operations = [
        migrations.CreateModel(
            name="aadhaarnumber",
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
                (
                    "useraadhaar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="votingApp.number1",
                    ),
                ),
            ],
        ),
    ]
