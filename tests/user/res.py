#!/usr/bin/env python
# coding=utf-8

"""Login resource rendering tests."""

import unittest as ut
from unittest.mock import patch, ANY, MagicMock

from bson import ObjectId
import json
from flask import abort

from app import app
import app.user.models as user


class LoginIndexTest(ut.TestCase):
    """GET Login resource should be generated."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch(
        "app.user.controllers.login.render_template",
        return_value="<body></body>"
    )
    def test_login_render(self, render_template):
        """GETting /u/login, render_template should be called."""
        with self.cli as cli:
            resp = cli.get("/u/login")
            self.assertEqual(resp.status_code, 200)
        render_template.assert_called_once_with("login.html", form=ANY)


class LoginPostTest(ut.TestCase):
    """POST login test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    @patch("app.user.controllers.login.Person")
    @patch("app.user.controllers.login.login_user")
    def test_post_login(self, login_user, Person, csrf):
        """
        Test POST /u/login.

        POSTing /u/login, the GETting /u/status, the user should
        og into the websote.
        """
        person = user.Person(email="test@example.com", id=ObjectId())
        Person.obejcts = MagicMock()
        Person.objects.get_or_404 = MagicMock(return_value=person)
        person.verify = MagicMock(return_value=True)
        req_data = {
            "email": "test@example.com",
            "password": "test"
        }
        with self.cli as cli:
            post_resp = cli.post("/u/login", data=req_data)
            self.assertEqual(post_resp.status_code, 200)
            self.assertEqual(post_resp.data, b"")
            self.assertEqual(post_resp.mimetype, "text/html")
            Person.objects.get_or_404.assert_called_once_with(
                email=person.email
            )
            person.verify.assert_called_once_with(req_data["password"])
            login_user.assert_called_once_with(person)

    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    @patch("app.user.controllers.login.Person")
    @patch("app.user.controllers.login.login_user")
    def test_post_logi_lack_formn(self, login_user, Person, csrf):
        """
        Test POST /u/login.

        POSTing /u/login, the GETting /u/status, should abort 417.
        """
        person = user.Person(email="test@example.com", id=ObjectId())
        Person.obejcts = MagicMock()
        Person.objects.get_or_404 = MagicMock(return_value=person)
        person.verify = MagicMock(return_value=True)
        req_data = {"email": "test@example.com"}
        with self.cli as cli:
            post_resp = cli.post("/u/login", data=req_data)
            self.assertEqual(post_resp.status_code, 417)
            self.assertEqual(post_resp.mimetype, "application/json")
            self.assertIn(
                "password", json.loads(post_resp.data.decode("utf-8"))
            )
            Person.objects.get_or_404.assert_not_called()
            person.verify.assert_not_called()
            login_user.assert_not_called()

    @patch("flask.ext.wtf.csrf.validate_csrf", return_value=True)
    @patch("app.user.controllers.login.Person")
    @patch("app.user.controllers.login.login_user")
    @patch("app.user.controllers.login.abort", side_effect=abort)
    def test_post_login_verify_failure(self, _abort, login_user, Person, csrf):
        """
        Test POST /u/login.

        POSTing /u/login, the GETting /u/status, proper user should be shown.
        """
        person = user.Person(email="test@example.com", id=ObjectId())
        Person.obejcts = MagicMock()
        Person.objects.get_or_404 = MagicMock(return_value=person)
        person.verify = MagicMock(return_value=False)
        req_data = {
            "email": "test@example.com",
            "password": "test"
        }
        with self.cli as cli:
            post_resp = cli.post("/u/login", data=req_data)
            self.assertEqual(post_resp.status_code, 404)
            Person.objects.get_or_404.assert_called_once_with(
                email=person.email
            )
            _abort.assert_called_once_with(404)
            person.verify.assert_called_once_with(req_data["password"])
            login_user.assert_not_called()


class StatusTest(ut.TestCase):
    """/u/login/status test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch("app.Person.objects")
    def test_session_status(self, user_objects):
        """GETting /u/login/status, current_user should be returned."""
        person = user.Person(
            id=ObjectId(),
            email="test@example.com",
            code="somethingnew",
            firstname="test", lastname="example",
            is_authenticated=True, is_active=True
        )
        user_objects.return_value.get = MagicMock(return_value=person)

        with self.cli as cli:
            with app.test_request_context():
                from flask import session
                from flask.ext.login import confirm_login
                session["user_id"] = person.get_id()
                confirm_login()
                with cli.session_transaction() as s:
                    s.update(session)
            resp = cli.get("/u/login/status")
            self.assertEqual(resp.status_code, 200)
            data = json.loads(resp.data.decode("utf-8"))
            excludes = [
                "code", "id", "is_authenticated", "is_active", "is_anonymous"
            ]
            for exclude in excludes:
                self.assertNotIn(exclude, data)


class LogoutTest(ut.TestCase):
    """[DELETE] /u/login test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()

    @patch("app.Person.objects")
    @patch("app.user.controllers.login.logout_user")
    def test_session_status(self, logout_user, user_objects):
        """GETting /u/login/status, current_user should be returned."""
        person = user.Person(
            id=ObjectId(),
            email="test@example.com",
            code="somethingnew",
            firstname="test", lastname="example",
            is_authenticated=True, is_active=True
        )
        user_objects.return_value.get = MagicMock(return_value=person)

        with self.cli as cli:
            with app.test_request_context():
                from flask import session
                from flask.ext.login import confirm_login
                session["user_id"] = person.get_id()
                confirm_login()

            resp = cli.delete("/u/login")
            logout_user.assert_called_once_with()
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.data, b"")
