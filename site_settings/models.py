from django.db import models

from wagtail.contrib.settings.models import BaseGenericSetting, register_setting
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField

@register_setting
class HoursSettings(BaseGenericSetting):
    """Hours area that end users could fill out."""

    hours = RichTextField(
        blank=True,
        null=True,
        features=[]
    )

    panels = [
        FieldPanel('hours')
    ]

@register_setting
class ContactSettings(BaseGenericSetting):
    """Contact area that end users could fill out."""

    contact = RichTextField(
        blank=True,
        null=True,
        features=['link']
    )

    panels = [
        FieldPanel('contact')
    ]


@register_setting
class SocialMediaSettings(BaseGenericSetting):
    """Social media setting config."""

    facebook = models.URLField(
        blank=True,
        help_text='Enter your facebook url'
    )
    twitter = models.URLField(
        blank=True,
        help_text='Enter your twitter url'
    )
    youtube = models.URLField(
        blank=True,
        help_text='Enter your youtube url'
    )
    instagram = models.URLField(
        blank=True,
        help_text='Enter your instagram url'
    )

    panels = [
        FieldPanel('facebook'),
        FieldPanel('twitter'),
        FieldPanel('youtube'),
        FieldPanel('instagram'),
    ]