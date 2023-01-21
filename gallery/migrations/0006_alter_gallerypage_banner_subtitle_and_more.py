# Generated by Django 4.1.4 on 2023-01-08 03:23

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0005_alter_gallerypage_cards"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallerypage",
            name="banner_subtitle",
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name="gallerypage",
            name="cards",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add your title", required=True
                                    ),
                                ),
                                (
                                    "cards",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "image",
                                                    wagtail.images.blocks.ImageChooserBlock(
                                                        required=True
                                                    ),
                                                ),
                                                (
                                                    "title",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=40, required=True
                                                    ),
                                                ),
                                                (
                                                    "text",
                                                    wagtail.blocks.TextBlock(
                                                        max_length=200, required=True
                                                    ),
                                                ),
                                                (
                                                    "button_one",
                                                    wagtail.blocks.PageChooserBlock(
                                                        required=False
                                                    ),
                                                ),
                                                (
                                                    "button_two",
                                                    wagtail.blocks.URLBlock(
                                                        help_text="If the button page above is selected, that will be used first.",
                                                        required=False,
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                            ]
                        ),
                    )
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
