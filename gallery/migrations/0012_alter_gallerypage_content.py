# Generated by Django 4.1.4 on 2023-01-15 14:38

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0011_alter_gallerypage_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gallerypage",
            name="content",
            field=wagtail.fields.StreamField(
                [
                    (
                        "cards",
                        wagtail.blocks.StructBlock(
                            [
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
                                            ]
                                        )
                                    ),
                                )
                            ]
                        ),
                    ),
                    (
                        "TitleAndSubtitle",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "title",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add title", required=True
                                    ),
                                ),
                                (
                                    "title_class_name",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("fw-light", "FW-LIGHT"),
                                            ("text-white", "TEXT-WHITE"),
                                        ]
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add subtitle", required=True
                                    ),
                                ),
                                (
                                    "subtitle_class_name",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("lead text-muted", "LEAD TEXT-MUTED"),
                                            ("text-muted", "TEXT-MUTED"),
                                        ]
                                    ),
                                ),
                                (
                                    "heading_level",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("h1", "H1"),
                                            ("h2", "H2"),
                                            ("h3", "H3"),
                                            ("h4", "H4"),
                                            ("h5", "H5"),
                                            ("h6", "H6"),
                                        ]
                                    ),
                                ),
                                (
                                    "button_url",
                                    wagtail.blocks.URLBlock(
                                        help_text="Add the url for the button",
                                        label="Button URL",
                                    ),
                                ),
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
