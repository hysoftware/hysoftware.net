#!/usr/bin/env python
# coding=utf-8

"""Admin panel home rendering tests."""
from unittest import TestCase
from unittest.mock import patch

from bson import ObjectId
from flask import abort, session
from flask.ext.login import confirm_login

from app import app
from app.user.models import Person


class UnauthenticatedRedirectTests(TestCase):
    """Return 404 for unauthorized user."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch("app.common.admin.abort", side_effect=abort)
    def test_abort(self, abort):
        """Return 404 for unauthorized user."""
        with self.cli as cli:
            resp = cli.get("/manage/")
            self.assertEqual(resp.status_code, 404)

        abort.assert_called_once_with(404)


class AuthenticatedAdminTests(TestCase):
    """Return 200 for authenticated user."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()
        self.person = Person(
            id=ObjectId(), is_authenticated=True, is_active=True,
            role=["admin"]
        )

    @patch("app.Person.objects")
    def test_authenticated(self, objects):
        """Return 200 for authenticated user."""
        objects.return_value.get.return_value = self.person
        with self.cli as cli:
            with app.test_request_context():
                session["user_id"] = self.person.get_id()
                confirm_login()
                with cli.session_transaction() as s:
                    s.update(session)
            resp = cli.get("/manage/")
            self.assertEqual(resp.status_code, 200)
        objects.return_value.get.called_once_with()


class AuthenticatedButNotHavePermissionTests(TestCase):
    """Return 404 (not 403) for not permitted user."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()
        self.person = Person(
            id=ObjectId(), is_authenticated=True, is_active=True,
            role=["member"]
        )

    @patch("app.Person.objects")
    def test_not_permitted(self, objects):
        """Return 404 for authenticated user."""
        objects.return_value.get.return_value = self.person
        with self.cli as cli:
            with app.test_request_context():
                session["user_id"] = self.person.get_id()
                confirm_login()
                with cli.session_transaction() as s:
                    s.update(session)
            resp = cli.get("/manage/")
            self.assertEqual(resp.status_code, 404)
        objects.return_value.get.called_once_with()
