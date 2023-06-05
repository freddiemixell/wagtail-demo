from django.db import models
from django.core.exceptions import ValidationError
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class ServiceListingPage(Page):
    subpage_types = ['services.ServicePage']
    max_count = 1
    template = 'services/service_listing_page.html'

    subtitle = models.TextField(
        blank=True,
        max_length=500,
    )
    content_panels = Page.content_panels + [
        FieldPanel('subtitle')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['services'] = ServicePage.objects.live().public()

        return context

class ServicePage(Page):
    parent_page_types = ['services.ServiceListingPage']
    template = 'services/service_page.html'

    description = models.TextField(
        blank=True,
        max_length=500
    )
    internal_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name="+",
        help_text='Select an internal wagtail page.',
        on_delete=models.SET_NULL
    )
    external_page = models.URLField(blank=True)
    button_text = models.CharField(
        blank=True,
        max_length=50
    )
    service_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=False,
        on_delete=models.SET_NULL,
        help_text='This image will be used on the Services Listing page and will be cropped to 570px by 370px.',
        related_name='+'
    )
    content_panels = Page.content_panels + [
        FieldPanel('description'),
        FieldPanel('internal_page'),
        FieldPanel('external_page'),
        FieldPanel('button_text'),
        FieldPanel('service_image'),
    ]

    def clean(self):
        super().clean()

        if self.internal_page and self.external_page:
            raise ValidationError({
                'internal_page': ValidationError("Please only select a page OR enter an external URL"),
                'external_page': ValidationError("Please only select a page OR enter an external URL")
            })
        
        if not self.internal_page and not self.external_page:
            raise ValidationError({
                'external_page': ValidationError("You must always select a page OR enter an external url."),
                'internal_page': ValidationError("You must always select a page OR enter an external url.")
            })