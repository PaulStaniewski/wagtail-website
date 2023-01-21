# Generated by Django 4.1.4 on 2023-01-07 02:36

from django.db import migrations, models
import django.db.models.deletion
import streams.blocks
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0078_referenceindex"),
    ]

    operations = [
        migrations.CreateModel(
            name="GalleryPage",
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
                (
                    "content",
                    wagtail.fields.StreamField(
                        [
                            (
                                "title_and_subtitle",
                                wagtail.blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail.blocks.CharBlock(
                                                help_text="Add title", required=True
                                            ),
                                        ),
                                        (
                                            "subtitle",
                                            wagtail.blocks.CharBlock(
                                                help_text="Add subtitle", required=True
                                            ),
                                        ),
                                    ],
                                    classname="title_and_subtitle",
                                ),
                            ),
                            ("full_richtext", streams.blocks.RichtextBlock()),
                        ],
                        blank=True,
                        null=True,
                        use_json_field=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Gallery page",
                "verbose_name_plural": "Gallery pages",
            },
            bases=("wagtailcore.page",),
        ),
    ]