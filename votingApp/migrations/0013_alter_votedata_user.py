# Generated by Django 4.2.1 on 2023-11-28 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0012_votedata_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="votedata", name="user", field=models.IntegerField(null=True),
        ),
    ]