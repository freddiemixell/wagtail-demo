from django.db import models

from django_extensions.db.fields import AutoSlugField

from modelcluster.models import ClusterableModel
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.models import Orderable

class MenuItem(Orderable):
    """Single menu item."""
    link_title = models.CharField(blank=True, max_length=50)
    link_url = models.CharField(max_length=500, blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        blank=True,
        null=True,
        related_name='+',
        on_delete=models.CASCADE
    )
    open_in_new_tab = models.BooleanField(default=True, blank=True)

    panels = [
        FieldPanel('link_title'),
        FieldPanel('link_url'),
        FieldPanel('link_page'),
        FieldPanel('open_in_new_tab'),
    ]

    page = ParentalKey("Menu", related_name="menu_items")

class Menu(ClusterableModel):
    """Main navigation."""
    title = models.CharField(
        max_length=100
    )
    slug = AutoSlugField(
        populate_from='title',
        editable=True
    )

    panels = [
        FieldPanel('title'),
        FieldPanel('slug'),
        InlinePanel('menu_items', label='Menu Items')
    ]

    def __str__(self):
        return self.title