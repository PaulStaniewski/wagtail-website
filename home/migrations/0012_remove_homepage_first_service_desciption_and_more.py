# Generated by Django 4.1.4 on 2023-01-09 09:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0011_alter_homepage_cards"),
    ]

    operations = [
        migrations.RemoveField(model_name="homepage", name="first_service_desciption",),
        migrations.RemoveField(model_name="homepage", name="first_service_title",),
        migrations.RemoveField(
            model_name="homepage", name="fourth_service_desciption",
        ),
        migrations.RemoveField(model_name="homepage", name="fourth_service_title",),
        migrations.RemoveField(
            model_name="homepage", name="second_service_desciption",
        ),
        migrations.RemoveField(model_name="homepage", name="second_service_title",),
        migrations.RemoveField(model_name="homepage", name="third_service_desciption",),
        migrations.RemoveField(model_name="homepage", name="third_service_title",),
    ]