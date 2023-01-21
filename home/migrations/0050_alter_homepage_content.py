# Generated by Django 4.1.4 on 2023-01-15 19:08

from django.db import migrations
import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0049_alter_homepage_content"),
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
                                        max_length=255, required=True
                                    ),
                                ),
                                (
                                    "subtitle",
                                    wagtail.blocks.CharBlock(
                                        max_length=255, required=True
                                    ),
                                ),
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                (
                                    "image_size",
                                    wagtail.blocks.ChoiceBlock(
                                        choices=[
                                            ("auto", "Auto"),
                                            ("cover", "Cover"),
                                            ("contain", "Contain"),
                                        ]
                                    ),
                                ),
                                (
                                    "button_url",
                                    wagtail.blocks.CharBlock(
                                        help_text="Add the url for the button",
                                        label="Button URL",
                                    ),
                                ),
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
                    (
                        "carousel",
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
                                    "images",
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
                                                    "caption",
                                                    wagtail.blocks.CharBlock(
                                                        max_length=255, required=False
                                                    ),
                                                ),
                                            ]
                                        )
                                    ),
                                ),
                                (
                                    "autoplay",
                                    wagtail.blocks.BooleanBlock(
                                        default=True,
                                        help_text="Autoplay the carousel on page load.",
                                        required=False,
                                    ),
                                ),
                                (
                                    "interval",
                                    wagtail.blocks.IntegerBlock(
                                        default=3000,
                                        help_text="Interval between slides in milliseconds.",
                                        required=False,
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "footer",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "year",
                                    wagtail.blocks.IntegerBlock(
                                        default="2023", required=True
                                    ),
                                ),
                                (
                                    "company_name",
                                    wagtail.blocks.CharBlock(
                                        default="Company Name", required=True
                                    ),
                                ),
                            ]
                        ),
                    ),
                    (
                        "testimonial",
                        wagtail.blocks.StructBlock(
                            [
                                (
                                    "image",
                                    wagtail.images.blocks.ImageChooserBlock(
                                        required=True
                                    ),
                                ),
                                ("name", wagtail.blocks.CharBlock(required=True)),
                                ("role", wagtail.blocks.CharBlock(required=True)),
                                ("quote", wagtail.blocks.TextBlock(required=True)),
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
