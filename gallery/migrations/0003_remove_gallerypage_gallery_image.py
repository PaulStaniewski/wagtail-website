# Generated by Django 4.1.4 on 2023-01-07 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0002_remove_gallerypage_content_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="gallerypage", name="gallery_image",),
    ]
