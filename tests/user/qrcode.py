#!/usr/bin/env python
# coding=utf-8

"""QRCode generator test."""

from unittest import TestCase
from unittest.mock import patch, MagicMock

from bson import ObjectId
from flask import session
from flask_login import confirm_login

from app import app
from app.user.models import Person


class QRCodeTest(TestCase):
    """/u/qrcode 404 test."""

    def setUp(self):
        """Setup."""
        app.testing = True
        self.cli = app.test_client()
        self.person = Person(
            id=ObjectId(),
            email="test@example.com",
            code="somethingnew",
            firstname="test", lastname="example",
            is_authenticated=True, is_active=True
        )
        self.secret = "TESTTESTTESTTEST"

    @patch("app.Person.objects")
    def test_qrcode_404(self, user_objects):
        """The resource should return 404 because there's no params."""
        user_objects.return_value.get = MagicMock(return_value=self.person)
        with self.cli as cli:
            with app.test_request_context():
                session["user_id"] = self.person.get_id()
                confirm_login()
                with cli.session_transaction() as s:
                    s.update(session)
            resp = cli.get("/u/qrcode")
            self.assertEqual(resp.status_code, 404)

    @patch("app.Person.objects")
    @patch("app.user.controllers.qrcode.OTPSecretKeyField")
    def test_qrcode_200(self, qrcode_generator, user_objects):
        """The resource should return SVG image for the qrcode."""
        user_objects.return_value.get = MagicMock(return_value=self.person)
        qrcode_generator.return_value.qrcode.return_value = "<svg></svg>"
        with self.cli as cli:
            with app.test_request_context():
                session["user_id"] = self.person.get_id()
                confirm_login()
                with cli.session_transaction() as s:
                    s.update(session)
            resp = cli.get(("/u/qrcode?secret={}").format(self.secret))
            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.mimetype, "image/svg+xml")
            self.assertEqual(
                resp.data, qrcode_generator.return_value.qrcode.return_value
            )
        qrcode_generator.assert_called_once_with()
        qrcode_generator.return_value.qrcode.assert_called_once_with(
            self.secret, name=self.person.email, issuer_name="HYSOFT"
        )
