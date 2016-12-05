#!/usr/bin/env python
# coding=utf-8

"""Setting test."""

from unittest.mock import patch

from django.test import TestCase


class ProductionConfigTest(TestCase):
    """Production Configuration Test."""

    def setUp(self):
        """Setup."""
        self.environ = {
            "SECRET": "test",
            "RECAPTCHA_PUBLIC_KEY": "recaptcha_test_pubkey",
            "RECAPTCHA_PRIVATE_KEY": "recaptcha_test_privkey",
            "MAILGUN_KEY": "mailgun-key",
            "MAILGUN_URL": "mailgun-url"
        }
        with patch.dict("os.environ", self.environ):
            from app.settings.public import PublicConfig
            self.conf_p = PublicConfig
        from app.settings.devel import DevelConfig
        self.conf_d = DevelConfig

    def test_subclass(self):
        """Production config should be a subclass of DevelConfig."""
        self.assertTrue(issubclass(self.conf_p, self.conf_d))

    def test_secret(self):
        """Secret key should be proper."""
        self.assertNotEqual(self.conf_p.SECRET_KEY, self.conf_d.SECRET_KEY)
        self.assertEqual(self.conf_p.SECRET_KEY, self.environ["SECRET"])

    def test_recaptcha(self):
        """Recaptcha secret and public should be proper."""
        self.assertNotEqual(
            self.conf_p.RECAPTCHA_PUBLIC_KEY,
            self.conf_d.RECAPTCHA_PUBLIC_KEY
        )
        self.assertEqual(
            self.conf_p.RECAPTCHA_PUBLIC_KEY,
            self.environ["RECAPTCHA_PUBLIC_KEY"]
        )
        self.assertNotEqual(
            self.conf_p.RECAPTCHA_PRIVATE_KEY,
            self.conf_d.RECAPTCHA_PRIVATE_KEY
        )
        self.assertEqual(
            self.conf_p.RECAPTCHA_PRIVATE_KEY,
            self.environ["RECAPTCHA_PRIVATE_KEY"]
        )

    def test_mailgun(self):
        """Mailgun test."""
        self.assertNotEqual(self.conf_p.MAILGUN_KEY, self.conf_d.MAILGUN_KEY)
        self.assertNotEqual(self.conf_p.MAILGUN_URL, self.conf_d.MAILGUN_URL)
        self.assertEqual(self.conf_p.MAILGUN_KEY, self.environ["MAILGUN_KEY"])
        self.assertEqual(self.conf_p.MAILGUN_URL, self.environ["MAILGUN_URL"])
