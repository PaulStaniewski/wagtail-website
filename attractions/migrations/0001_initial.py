# Generated by Django 4.1.4 on 2023-01-05 04:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="AttractionPage",
            fields=[
                (
                    "page_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="wagtailcore.page",
                    ),
                ),
                ("title_of_attraction", models.CharField(max_length=100, null=True)),
            ],
            options={
                "verbose_name": "Attraction page",
                "verbose_name_plural": "Attraction pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]