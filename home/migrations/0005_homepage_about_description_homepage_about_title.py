# Generated by Django 4.1.4 on 2023-01-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0004_homepage_banner_subtitle"),
    ]

    operations = [
        migrations.AddField(
            model_name="homepage",
            name="about_description",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="homepage",
            name="about_title",
            field=models.CharField(max_length=100, null=True),
        ),
    ]
