#!/usr/bin/env python
# coding=utf-8

"""Env config tests."""

import sys
import os

from unittest import TestCase


class EnvironmentTestBase(TestCase):
    """
    Test Environment configurations.

    Note that this is just an base
    """

    def setUp(self):
        """Setup."""
        if type(self) is EnvironmentTestBase:
            raise TypeError("This class is abstract class")
        self.env_backup = os.environ.get("mode", None)

    def tearDown(self):
        """Tear down."""
        if self.env_backup:
            os.environ["mode"] = self.env_backup
        else:
            os.environ.pop("mode", None)

        sys.modules.pop("app.config", None)


class DevelopmentTestClass(EnvironmentTestBase):
    """Development Mode Test."""

    def setUp(self):
        """Setup."""
        super(DevelopmentTestClass, self).setUp()
        os.environ["mode"] = "devel"

    def test_development_mode(self):
        """Devel Config should be read."""
        from app.config import DevelConfig
        self.assertIsNotNone(DevelConfig)

    def test_production_mode(self):
        """Production config should raise an error."""
        with self.assertRaises(ImportError):
            from app.config import ProductionConfig
            self.assertIsNone(ProductionConfig)


class ProductionTestClass(EnvironmentTestBase):
    """Test Development Mode."""

    def setUp(self):
        """Setup."""
        super().setUp()
        os.environ["mode"] = "production"
        os.environ["secret"] = \
            os.environ["recaptcha_prikey"] = \
            os.environ["recaptcha_pubkey"] = \
            os.environ["MAILGUN_API"] = \
            os.environ["MAILGUN_URL"] = "test"

    def test_production_mode(self):
        """Production Config should be read."""
        from app.config import ProductionConfig
        self.assertIsNotNone(ProductionConfig)

    def test_devel_mode(self):
        """Devel config should raise an error."""
        with self.assertRaises(ImportError):
            from app.config import DevelConfig
            self.assertIsNone(DevelConfig)
