# Generated by Django 4.2.1 on 2023-11-27 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0005_aadhaarnumber_otp"),
    ]

    operations = [
        migrations.AlterField(
            model_name="aadhaarnumber",
            name="useraadhaar",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
