#!/usr/bin/env python
# coding=utf-8

"""Env config tests."""

import os
import sys

from unittest import TestCase
from unittest.mock import patch


class DevelopmentTestClass(TestCase):
    """Development Mode Test."""

    def setUp(self):
        """Setup."""
        self.env = patch.dict(os.environ, {"mode": "devel"})

    def tearDown(self):
        """Teardown."""
        sys.modules.pop("app.config", None)

    def test_development_mode(self):
        """Devel Config should be read."""
        with self.env:
            from app.config import DevelConfig
            self.assertIsNotNone(DevelConfig)

    def test_production_mode(self):
        """Production config should raise an error."""
        with self.env:
            with self.assertRaises(ImportError):
                from app.config import ProductionConfig
                self.assertIsNone(ProductionConfig)


class ProductionTestClass(TestCase):
    """Test Development Mode."""

    def setUp(self):
        """Setup."""
        env = {"mode": "production"}
        env.update({
            key: "test"
            for key in [
                "secret", "recaptcha_prikey", "recaptcha_pubkey",
                "MAILGUN_API", "MAILGUN_URL"
            ]
        })
        self.env = patch.dict(os.environ, env)

    def tearDown(self):
        """Teardown."""
        sys.modules.pop("app.config", None)

    def test_production_mode(self):
        """Production Config should be read."""
        with self.env:
            from app.config import ProductionConfig
            self.assertIsNotNone(ProductionConfig)

    def test_devel_mode(self):
        """Devel config should raise an error."""
        with self.env:
            with self.assertRaises(ImportError):
                from app.config import DevelConfig
                self.assertIsNone(DevelConfig)


class InvalidModeTest(TestCase):
    """Test Invalid mode."""

    def test_invalid_mode_config(self):
        """Config should raise Invalid mode is given error."""
        with patch.dict(os.environ, {"mode": "hahaha"}):
            with self.assertRaises(EnvironmentError) as e:
                import app.config  # noqa

        self.assertEqual(str(e.exception), "Invalid mode is given.")
