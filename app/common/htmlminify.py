#!/usr/bin/env python
# coding=utf-8

"""HTML minification function."""

import htmlmin


def minify_html(html_to_minify):
    """
    Minify the given html.

    Paramters:
        html_to_minify: The HTML to minify.
    """
    return htmlmin.minify(
        html_to_minify,
        remove_comments=True,
        remove_empty_space=True,
        remove_optional_attribute_quotes=False
    )
