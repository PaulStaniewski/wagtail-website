# Generated by Django 4.1.4 on 2023-01-07 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("attractions", "0009_gallerypage"),
    ]

    operations = [
        migrations.DeleteModel(name="GalleryPage",),
    ]