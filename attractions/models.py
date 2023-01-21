"""Attraction page."""
from django.db import models
from wagtail.core.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField

from streams import blocks

class AttractionPage(Page):
    """ Attraction page class. """

    template = "attractions/attraction_page.html"    

    content = StreamField(
        [   
            ("title_and_subtitle", blocks.TitleAndSubtitle(classname="title_and_subtitle")),
            ("full_richtext", blocks.RichtextBlock()),
            ("cards", blocks.ImageSection()),
            ("banner", blocks.BannerBlock()),            
            ("carousel", blocks.CarouselBlock()),
            ("footer", blocks.Footer()),
            ("news_section", blocks.NewsSection())
            
        ],
        null=True,
        blank=True,
        use_json_field=True)    

    content_panels = Page.content_panels + [        
        FieldPanel("content"),        
    ]

    class Meta:
        verbose_name = "Attraction page"
        verbose_name_plural = "Attraction pages"

    