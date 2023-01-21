"""Streamfields live in here"""

from wagtail.core import blocks

from wagtail.images.blocks import ImageChooserBlock


class BannerBlock(blocks.StructBlock):
    """
    A banner block that allows the user to add a title, subtitle, and background image.
    """
    title = blocks.CharBlock(required=True, max_length=255)
    subtitle = blocks.CharBlock(required=True, max_length=255)
    image = ImageChooserBlock(required=True)    
    image_size = blocks.ChoiceBlock(choices=[
        ('auto', 'Auto'),
        ('cover', 'Cover'),
        ('contain', 'Contain'),
    ], default='cover', required=True)

    button_url = blocks.CharBlock(label="Button URL", help_text='Add the url for the button')

    class Meta:
        template = "streams/banner.html"
        icon = "image"
        label = "Banner"


class ImageSection(blocks.StructBlock):
    """ 
    Image Section with description
    """  
   
    card = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),                
            ]
        )
    )

    class Meta:
        template = "streams/image_block.html"
        icon = "edit"
        label = "Attractions"    

class CarouselBlock(blocks.StructBlock):
    """
    A carousel block that allows the user to add images and captions to the carousel.
    """

    title = blocks.CharBlock(required=True, help_text='Add title')
    subtitle = blocks.CharBlock(required=True, help_text='Add subtitle')  


    images = blocks.ListBlock(
        blocks.StructBlock([
            ('image', ImageChooserBlock(required=True)),
            ('caption', blocks.CharBlock(required=False, max_length=255)),
        ])
    )
    autoplay = blocks.BooleanBlock(
        required=False,
        default=True,
        help_text='Autoplay the carousel on page load.'
    )
    interval = blocks.IntegerBlock(
        required=False,
        default=3000,
        help_text='Interval between slides in milliseconds.'
    )

    class Meta:
        template = "streams/carousel.html"
        icon = "image"
        label = "Carousel"
              

class TitleAndSubtitle(blocks.StructBlock):
    """Title and subtitle"""

    title = blocks.CharBlock(required=True, help_text='Add title') 

    title_class_name = blocks.ChoiceBlock(choices=[
        ('fw-light', 'FW-LIGHT'),
        ('text-white', 'TEXT-WHITE'),
    ])  

    subtitle = blocks.CharBlock(required=True, help_text='Add subtitle')   

    subtitle_class_name = blocks.ChoiceBlock(choices=[
        ('lead text-muted', 'LEAD TEXT-MUTED'),
        ('text-muted', 'TEXT-MUTED'),
    ])

    heading_level = blocks.ChoiceBlock(choices=[
        ('h1', 'H1'),
        ('h2', 'H2'),
        ('h3', 'H3'),
        ('h4', 'H4'),
        ('h5', 'H5'),
        ('h6', 'H6'),
    ], default='h1')         

    class Meta:
        template = "streams/title_subtitle.html"
        icon = "edit"
        label = "Title & subtitle"             

class RichtextBlock(blocks.RichTextBlock):
    """Richtext with all the features"""

    class Meta:
        template = "streams/richtext_block.html"
        icon = "edit"
        label = "Full RichText"

class CardBlock(blocks.StructBlock):
    """ Image and description"""    
   
    cards = blocks.ListBlock(
        blocks.StructBlock(
            [
                ("image", ImageChooserBlock(required=True)),
                ("title", blocks.CharBlock(required=True, max_length=40)),
                ("text", blocks.TextBlock(required=True, max_length=200)),
                
            ]
        )
    )

    class Meta:
        template = "streams/card_block.html"
        icon = "placeholder"
        label = "Images"


class Footer(blocks.StructBlock):
    ''' Footer block '''

    year = blocks.IntegerBlock(required=True, default='2023')
    company_name = blocks.CharBlock(required=True, default='Company Name')

    class Meta:
        template = "streams/footer.html"    

class NewsSection(blocks.StructBlock):
    """News section with title, description and list of articles"""

    title = blocks.CharBlock(required=True)
    description = blocks.RichTextBlock(required=True, help_text='Add a short description of the news section')
    articles = blocks.ListBlock(blocks.StructBlock([
        ('title', blocks.CharBlock(required=True)),
        ('date', blocks.DateBlock(required=True)),
        ('image', ImageChooserBlock()),
        ('summary', blocks.RichTextBlock(required=True)),        
    ]))

    class Meta:
        template = 'streams/news_section.html'
        icon = 'folder-open'
        label = 'News Section'
