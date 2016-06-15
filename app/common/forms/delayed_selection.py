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

    @property
    def choices(self):
        """
        Return choices.

        CAUTION: This setter and getter is not symmetric; setter sets the
            value directly while getter calls the value if it is callable.
        """
        choices = None
        try:
            choices = self._choices()
        except TypeError:
            choices = self._choices
        return choices

    @choices.setter
    def choices(self, value):
        """
        Set choices.

        CAUTION: This setter and getter is not symmetric; setter sets the
            value directly while getter calls the value if it is callable.
        """
        self._choices = value

    @property
    def choices_dict(self):
        """
        Return the mapper from value to label.

        Return Value: A dict that has `value` as its key, and `label` as
            its value.
        """
        return dict(self.choices)
