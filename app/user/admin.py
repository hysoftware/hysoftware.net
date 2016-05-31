#!/usr/bin/env python
# coding=utf-8

"""Admin panel."""

from collections import OrderedDict

from flask.ext.admin.form import rules
import wtforms.fields as fld
import wtforms.validators as vld

from ..common import AdminModelBase


class PersonAdmin(AdminModelBase):
    """Person admin."""

    form_subdocuments = {
        "skills": {
            "form_subdocuments": {
                None: {
                    "form_rules": (
                        "language", "frameworks", rules.HTML("<hr>")
                    )
                }
            }
        }
    }
    column_exclude_list = ("code", )
    form_excluded_columns = ("code", )
    form_extra_fields = OrderedDict([
        ("current_password", fld.PasswordField()),
        (
            "new_password",
            fld.PasswordField(validators=[vld.EqualTo("new_password")])
        ), (
            "confirm_password",
            fld.PasswordField(validators=[vld.EqualTo("new_password")])
        )
    ])
