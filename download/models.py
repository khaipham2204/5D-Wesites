from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models
from wagtail.core.models import Page
from wagtail.search import index


class Download(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]
