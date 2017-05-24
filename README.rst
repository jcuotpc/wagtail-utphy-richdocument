utphy richdocument
==================

This is a wagtail app to be applied on wagtail generic docs.
It adds the following streamfield blocks:

- doc_byline
- body_text
- quote
- bustout
- code_chunk
- math_formula
- table
- media_embed

Dependencies
------------

- wagtail_

.. _wagtail: https://wagtail.io

Quick Start
-----------
install from pypy::

    pip install wagtail-utphy-richdocument

add "utphy_richdocument" and "wagtail.contrib.table_block" to your INSTALLED_APPS setting::

    INSTALLED_APPS = [
        ...
        'wagtail.contrib.table_block',
        'utphy_richdocument',
    ]

* In your own app create a new model which subclasses the StreamFieldDoc model.

*models.py*::

    from utphy_richdocument.models import StreamFieldDoc
    from wagtail.wagtailadmin.edit_handlers import StreamFieldPanel

    class YourModel(StreamFieldDoc):
        template = 'path_to_your_template.html'

        content_panels = Page.content_panels + [
            # your_model_fields
            StreamFieldPanel('body'),
    ]

* In your template, make sure you have the following snippet:

*path_to_your_template.py*::

    {% for block in self.body %}
      {{block}}
    {% endfor %}

Finally run::

    python manage.py collectstatic
    python manage.py makemigrations
    python manage.py migrate
