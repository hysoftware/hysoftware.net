#!/usr/bin/env python
# coding=utf-8

import htmlmin


def minify_html(html_to_minify):
    return htmlmin.minify(
        html_to_minify,
        remove_comments=True,
        remove_empty_space=True,
        remove_optional_attribute_quotes=False
    )
