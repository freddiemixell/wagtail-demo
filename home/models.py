from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock

from streams import blocks


class HomePage(Page):
    lead_text = models.CharField(
        max_length=140,
        blank=True,
        help_text='Subheading under the banner title')

    button = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        help_text='Select an optional page to link to.',
        on_delete=models.SET_NULL)

    button_text = models.CharField(
        max_length=50,
        default='Read more',
        blank=False,
        help_text='Button text')

    banner_background_image = models.ForeignKey(
        'wagtailimages.Image',
        blank=False,
        null=True,
        related_name='+',
        help_text='The banner background image.',
        on_delete=models.SET_NULL)

    body = StreamField([
            ('title', blocks.TitleBlock()),
            ('cards', blocks.CardsBlock()),
            ('image_and_text', blocks.ImageAndTextBlock()),
            ('call_to_action', blocks.CallToActionBlock()),
            ('testimonial', SnippetChooserBlock(
                target_model='testimonials.Testimonial',
                template='streams/testimonial_block.html'
            ))
        ],
        use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('lead_text'),
        FieldPanel('button'),
        FieldPanel('button_text'),
        FieldPanel('banner_background_image'),
        FieldPanel('body')]
