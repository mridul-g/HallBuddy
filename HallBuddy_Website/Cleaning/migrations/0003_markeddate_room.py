# Generated by Django 5.0.3 on 2024-03-18 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Cleaning", "0002_markeddate_user_name"),
    ]

    operations = [
        migrations.AddField(
            model_name="markeddate",
            name="room",
            field=models.CharField(default="NA", max_length=10),
        ),
    ]