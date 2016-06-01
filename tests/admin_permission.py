#!/usr/bin/env python
# coding=utf-8

"""Admin permission check."""

import mongoengine as db
import unittest as ut
from unittest.mock import patch

from flask.ext.login import login_user
from bson import ObjectId
from app import app
from app.user.models import Person
from app.common import AdminModelBase


class AccessibleCheck(ut.TestCase):
    """Test in the case that `Person` has `admin` role."""

    def setUp(self):
        """Setup."""
        app.testing = True

    def test_accessible(self):
        """Calling admin.is_accessible, it should return True."""
        with app.test_request_context():
            login_user(Person(
                is_authenticated=True, is_active=True, id=ObjectId(),
                role=["normal", "admin"]
            ))
            admin = AdminModelBase(type("Document", (db.Document, ), {}))
            self.assertTrue(admin.is_accessible())

    def test_inaccessible(self):
        """Calling admin.is_accessible, it should return False."""
        with app.test_request_context():
            login_user(Person(
                is_authenticated=True, is_active=True, id=ObjectId(),
                role=["normal", "developer"]
            ))
            admin = AdminModelBase(type("Document", (db.Document, ), {}))
            self.assertFalse(admin.is_accessible())

    def test_not_authenticated(self):
        """Calling admin.is_accessible, it should return False."""
        with app.test_request_context():
            login_user(Person(
                is_authenticated=False, is_active=True, id=ObjectId(),
                role=["normal", "admin"]
            ))
            admin = AdminModelBase(type("Document", (db.Document, ), {}))
            self.assertFalse(admin.is_accessible())


class InaccessibleCallbackCheck(ut.TestCase):
    """Inaccessible callback check."""

    @patch("app.common.admin.redirect")
    def test_redirect(self, redirect):
        """Redirect should be called with `/#/`."""
        admin = AdminModelBase(type("Document", (db.Document, ), {}))
        admin.inaccessible_callback(None)
        redirect.assert_called_once_with("/#/")
