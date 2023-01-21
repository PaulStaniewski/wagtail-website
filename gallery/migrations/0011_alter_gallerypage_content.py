# Generated by Django 4.1.4 on 2023-01-15 11:02

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("gallery", "0010_remove_gallerypage_album_name_and_more"),
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
                                ("title", wagtail.blocks.CharBlock(required=True)),
                                (
                                    "subtitle",
                                    wagtail.blocks.RichTextBlock(
                                        help_text="Add subtitle", required=True
                                    ),
                                ),
                                (
                                    "title_class_name",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("fw-light", "FW-LIGHT"),
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