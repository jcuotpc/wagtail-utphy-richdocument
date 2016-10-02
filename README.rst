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

1. add "utphy_richdocument" to your INSTALLED_APPS setting::

    INSTALLED_APPS = [
        ...
        'utphy_richdocument',
    ]

2. In your own app create a new model which subclasses the StreamFieldDoc model::

    from utphy_richdocument.models import StreamFieldDoc

    class YourModel(StreamFieldDoc):
        template = 'path_to_your_template.html'

3. Run `python manage.py collectstatic` to collect the static files from the app into your own static section.

4. Run `python manage.py migrate` to update the tables in your app.
