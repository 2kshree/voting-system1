# Generated by Django 4.2.1 on 2023-11-27 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0006_alter_aadhaarnumber_useraadhaar"),
    ]

    operations = [
        migrations.CreateModel(
            name="voteringlist",
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
                ("image", models.ImageField(upload_to="img/%y")),
                ("leadername", models.CharField(max_length=10, null=True)),
                ("Foundation_name", models.CharField(max_length=10, null=True)),
            ],
        ),
    ]
