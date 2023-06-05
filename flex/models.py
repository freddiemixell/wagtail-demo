from wagtail.models import Page
from wagtail.fields import StreamField
from wagtail.snippets.blocks import SnippetChooserBlock
from wagtail.admin.panels import FieldPanel
from wagtail import blocks as wagtail_blocks

from streams import blocks

class FlexPage(Page):

    body = StreamField([
            ('title', blocks.TitleBlock()),
            ('cards', blocks.CardsBlock()),
            ('image_and_text', blocks.ImageAndTextBlock()),
            ('call_to_action', blocks.CallToActionBlock()),
            ('testimonial', SnippetChooserBlock(
                target_model='testimonials.Testimonial',
                template='streams/testimonial_block.html'
            )),
            ('pricing_table', blocks.PricingTableBlock()),
            ('rich_text', wagtail_blocks.RichTextBlock(
                template='streams/simple_richtext_block.html',
                features=['bold', 'italic', 'ol', 'ul', 'link']
            ))
        ],
        use_json_field=True, null=True, blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')]
    
    class Meta:
        verbose_name = 'Flex (misc) page'
        verbose_name_plural = 'Flex (misc) pages'