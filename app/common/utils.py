#!/usr/bin/env python
# coding=utf-8


"""Commonly used uitls."""


def gen_uuid_pattern(param=None):
    """Generate UUID Pattern with given param."""
    return (
        r"(?P<" + param +
        ">[a-zA-Z0-9]{8}(?:-[a-zA-Z0-9]{4}){3}-[a-zA-Z0-9]{12})"
    ) if param else (
        r"([a-zA-Z0-9]{8}(?:-[a-zA-Z0-9]{4}){3}-[a-zA-Z0-9]{12})"
    )
