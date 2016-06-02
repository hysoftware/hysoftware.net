#!/usr/bin/env python
# coding=utf-8

"""Selection Field with delayed choice evaluation."""
import wtforms.fields as fld


class DelayedSelectField(fld.SelectField):
    """Selection Field with delayed choice evaluation."""

    def __init__(self, *args, **kwargs):
        """
        Init the class.

        Parameters:
            *args, *kwargs: Any arguments to be passed to super class.
        """
        super(DelayedSelectField, self).__init__(*args, **kwargs)

    def iter_choices(self):
        """Yeild the choice."""
        choices = None
        try:
            choices = self.choices()
        except TypeError:
            choices = self.choices

        for (value, label) in choices:
            yield (value, label, self.coerce(value) == self.data)
