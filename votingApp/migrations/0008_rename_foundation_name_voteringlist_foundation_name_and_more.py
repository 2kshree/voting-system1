# Generated by Django 4.2.1 on 2023-11-27 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("votingApp", "0007_voteringlist"),
    ]

    operations = [
        migrations.RenameField(
            model_name="voteringlist",
            old_name="Foundation_name",
            new_name="foundation_name",
        ),
        migrations.AddField(
            model_name="voteringlist",
            name="code",
            field=models.IntegerField(null=True),
        ),
    ]