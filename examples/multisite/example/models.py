from django.utils import translation
from django.http import HttpResponseRedirect
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailadmin.edit_handlers import FieldPanel, StreamFieldPanel


class LanguageRedirectionPage(Page):
    def serve(self, request):
        language = translation.get_language_from_request(request)
        return HttpResponseRedirect(self.url + language + '/')


class AbstractExamplePage(Page):
    body = StreamField([
        ('paragraph', blocks.RichTextBlock())
    ])

    content_panels = [
        FieldPanel('title'),
        StreamFieldPanel('body')
    ]

    class Meta:
        abstract = True


class HomePage(AbstractExamplePage):
    pass


class GenericPage(AbstractExamplePage):
    pass


class BlogListPage(AbstractExamplePage):
    pass


class BlogPostPage(AbstractExamplePage):
    pass
