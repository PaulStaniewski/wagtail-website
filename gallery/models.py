""" Gallery page """
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from streams import blocks

class GalleryPage(Page):
    """ Gallery page class. """

    template = "gallery/gallery.html"
        

    # Gallery Section

    content = StreamField(
        [
            ("cards", blocks.CardBlock()),
            ("TitleAndSubtitle", blocks.TitleAndSubtitle()),
            ("footer", blocks.Footer())
        ],
        null=True,
        blank=True,
        use_json_field=True
    )    

    content_panels = Page.content_panels + [               
        FieldPanel("content"),              
    ]

    class Meta:
        verbose_name = "Gallery page"
        verbose_name_plural = "Gallery pages"    
