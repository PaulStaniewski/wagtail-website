# Generated by Django 4.1.4 on 2023-01-05 08:01

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ("wagtailimages", "0024_index_image_file_hash"),
        ("attractions", "0004_attractionpage_description_of_attraction"),
    ]

    operations = [
        migrations.AddField(
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
                                        help_text="Add Your title", required=True
                                    ),
                                ),
                                (
                                    "text",
                                    wagtail.blocks.TextBlock(
                                        help_text="Add additional text", required=True
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
        migrations.AlterField(
            model_name="attractionpage",
            name="description_of_attraction",
            field=models.TextField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name="attractionpage",
            name="image_of_attraction",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="wagtailimages.image",
            ),
        ),
    ]
