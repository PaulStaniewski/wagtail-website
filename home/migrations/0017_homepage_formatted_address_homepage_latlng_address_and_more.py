# Generated by Django 4.1.4 on 2023-01-09 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0016_mappage"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="formatted_address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="latlng_address",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.DeleteModel(name="MapPage",),
    ]
