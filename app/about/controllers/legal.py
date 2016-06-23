#!/usr/bin/env python
# coding=utf-8

"""Legal notification page controller."""

from flask import render_template, url_for
from flask.ext.classy import FlaskView


class LegalView(FlaskView):
    """Legal Notation."""

    trailing_slash = False

    # Note: How to write tab-structure
    # The tab structure is depending on regulations variable that is
    # typed as tuple.
    # In the list, there are single/multiple tuples with 4 elements.
    # 1st is the ID to distinguish what is "what"
    # 2nd is the title to be showen at the title tab.
    # 3rd is the template file to be placed to the pane.
    # 4th is True if the tab should be active, False Otherwiese.
    # Note that specifying True at 4th argument must be specified "once".
    regulations = (
        (
            "scta",
            "Notation based on the Specified Commercial Transaction Act",
            "scta.html", True
        ), (
            "copyrights",
            "Copyrights",
            "copyrights.html", False
        )
    )

    def index(self):
        """Render Legal Notation."""
        # Note: Asset Copyrights
        # This website is using free-assets, so needs to add copyrights url or
        # something to specify the rights.
        assets_info = (
            {
                "asset": {
                    "url": url_for(
                        "home.static", filename="forest_retina.jpg"
                    ),
                    "name": "forest_retina.jpg"
                },
                "license": "CC0",
                "page": {
                    "url": "http://alana.io/downloads/green-trees-grass/",
                    "name": "Alana.io"
                }
            }, {
                "asset": {
                    "url": url_for(
                        "about.static", filename="coffee_retina.jpg"
                    ),
                    "name": "coffee_retina.jpg"
                },
                "license": "CC0",
                "page": {
                    "url": (
                        "http://alana.io/downloads/coffee-latte-cappuccino-2/"
                    ),
                    "name": "Alana.io"
                }
            }, {
                "asset": {
                    "url": url_for(
                        "about.static", filename="book_retina.jpg"
                    ),
                    "name": "book_retina.jpg"
                },
                "license": "CC0",
                "page": {
                    "url": "http://alana.io/downloads/book-3/",
                    "name": "Alana.io"
                }
            }, {
                "asset": {
                    "url": url_for(
                        "contact.static", filename="cafe_retina.jpg"
                    ),
                    "name": "cafe_retina.jpg"
                },
                "license": "CC0",
                "page": {
                    "url": (
                        "http://alana.io/downloads/macbook-laptop-computer-38/"
                    ),
                    "name": "Alana.io"
                }
            }, {
                "asset": {
                    "url": "https://www.google.com/fonts/specimen/Open+Sans",
                    "name": "Open Sans"
                },
                "license": "Apache License, version 2.0",
                "page": {
                    "url": "https://www.google.com/fonts/specimen/Open+Sans",
                    "name": "Google Fonts"
                }
            }
        )
        return render_template(
            "legal.html", regulations=self.regulations,
            assets_info=assets_info
        )
