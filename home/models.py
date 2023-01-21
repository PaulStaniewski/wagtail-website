from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.core.fields import StreamField
from streams import blocks

class HomePage(Page):
    """Home page model."""

    templates = "templates/home/home_page.html"     

    content = StreamField(
        [   
            ("banner", blocks.BannerBlock()),                        
            ("cards", blocks.ImageSection()),
            ("carousel", blocks.CarouselBlock()),
            ("footer", blocks.Footer()),           
                               
        ],
        null=True,
        blank=True,
        use_json_field=True
    )    
   
    content_panels = Page.content_panels + [      
                       
        FieldPanel("content"),               
    ]