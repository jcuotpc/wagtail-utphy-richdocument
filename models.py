from __future__ import unicode_literals

from django.utils.encoding import force_text

from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.wagtailadmin.edit_handlers import (StreamFieldPanel)
from wagtail.wagtailcore import blocks
from wagtail.wagtailcore.fields import StreamField
from wagtail.wagtailcore.models import Page
from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtailsearch import index


class CodeBlock(blocks.StructBlock):
    LANGUAGES = (
        ('cpp', 'C++'),
        ('cs', 'C#'),
        ('html', 'Html'),
        ('js', 'JavaScript'),
        ('python', 'Python'),
        # Each code block is tagged with the language used so highlight.js
        # marks the code up correctly
    )

    code = blocks.TextBlock(max_length=8000, rows=10, blank=False, null=False)
    language = blocks.ChoiceBlock(choices=LANGUAGES, required=False,
                                  default='python')

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/code.html'
        icon = 'code'
        label = 'Code chunk'


class MathBlock(blocks.StructBlock):
    math = blocks.TextBlock(max_length=8000, blank=False, null=False)

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/math.html'
        icon = 'code'
        label = 'Math formula'


default_table_options = {
    'minSpareRows': 0,
    'startRows': 3,
    'startCols': 3,
    'colHeaders': False,
    'rowHeaders': False,
    'contextMenu': True,
    'editor': 'text',
    'stretchH': 'all',
    'height': 108,
    'renderer': 'text',
    'autoColumnSize': False,
}


class TableBlock(blocks.StreamBlock):
    table = TableBlock(table_options=default_table_options)

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        icon = 'table'


class VideoBlock(blocks.StructBlock):
    title = blocks.CharBlock()
    video_url = blocks.URLBlock(
        help_text='Insert full URL of'
                  ' embedded video here. '
                  'Ex. https://www.youtube.com/embed/sdfk343244dfef5'
    )
    allow_full_screen = blocks.BooleanBlock(required=False, default=True)

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/utmedia.html'
        icon = 'media'
        label = "UofT My Media"


class QuoteBlock(blocks.StructBlock):
    quote = blocks.TextBlock(max_length=500, rows=5, blank=False, null=False)
    author = blocks.CharBlock(max_length=100, blank=True, null=True)
    author_url = blocks.URLBlock(required=False)

    # todo: add background color chooser

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/quote.html'
        icon = 'openquote'


class DocBylineBlock(blocks.StructBlock):
    text = blocks.TextBlock(max_length=100, rows=2, required=False)

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/doc_byline.html'
        icon = 'snippet'


class BustoutBlock(blocks.StructBlock):
    text = blocks.TextBlock(max_length=500, rows=5)
    image = ImageChooserBlock(
        help_text="size of image should be at least 500px x 500px large")

    # todo: add background color chooser
    # todo: add image position chooser

    def get_searchable_content(self, value):
        return [force_text(value)]

    class Meta:
        template = 'utphy_richdocument/blocks/bustout.html'
        icon = 'image'


# todo: create carousel block

BLOCK_TYPES = [
    ('doc_byline', DocBylineBlock()),
    ('body_text', blocks.RichTextBlock(icon='doc-full',
                                       required=True, classname="paragraph",
                                       help_text="For inline formulas you can "
                                                 "use \(....\)")),
    ('quote', QuoteBlock()),
    ('bustout', BustoutBlock()),
    ('code_chunk', CodeBlock()),
    ('math_formula', MathBlock()),
    ('table', TableBlock()),
    ('media_embed', VideoBlock()),
]


class StreamFieldDoc(Page):
    body = StreamField(
        block_types=BLOCK_TYPES,
        null=True,
        blank=True,
        verbose_name='Content')

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]



    class Meta:
        abstract = True
