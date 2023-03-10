# Generated by Django 4.1.4 on 2023-01-11 18:57

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
import wagtail_icon_picker.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0035_homepage_icon_alter_homepage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="homepage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "banner",
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
                            ]
                        ),
                    ),
                    (
                        "about",
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
                            ]
                        ),
                    ),
                    (
                        "service",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "card",
                                    wagtail.blocks.ListBlock(
                                        wagtail.blocks.StructBlock(
                                            [
                                                (
                                                    "main_title",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=40, required=True
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
                                                    "icon",
                                                    wagtail_icon_picker.blocks.BootstrapIconPickerBlock(),
                                                ),
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "card",
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
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                ],
                blank=True,
                null=True,
                use_json_field=True,
            ),
        ),
    ]
