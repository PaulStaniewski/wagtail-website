# Generated by Django 4.1.4 on 2023-01-05 08:59

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        (
            "attractions",
            "0006_remove_attractionpage_description_of_attraction_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="attractionpage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "title_and_text",
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
                                (
                                    "text",
                                    wagtail.blocks.TextBlock(
                                        help_text="Add additional text", required=True
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        help_text="Add image", required=False
                                    ),
                                ),
                            ],
                            classname="text_and_title",
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
