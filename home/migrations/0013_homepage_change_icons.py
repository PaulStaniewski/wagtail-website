# Generated by Django 4.1.4 on 2023-01-09 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0012_remove_homepage_first_service_desciption_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="change_icons",
            field=models.CharField(max_length=10, null=True),
        ),
    ]
