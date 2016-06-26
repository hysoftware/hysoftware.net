#!/usr/bin/env python
# coding=utf-8

"""DB Authorization Tests."""

import os
import sys

from unittest import TestCase
from unittest.mock import patch


class DBAuthTest(TestCase):
    """DB Authorization test."""

    def setUp(self):
        """Setup function."""
        env = {
            "mode": "production",
            "db_url": "mongodb://mongodb/test",
            "db_user": "testUser",
            "db_password": "testPassword"
        }
        env.update({
            key: "test"
            for key in [
                "secret", "recaptcha_prikey", "recaptcha_pubkey",
                "MAILGUN_API", "MAILGUN_URL"
            ]
        })
        self.env = patch.dict(os.environ, env)
        sys.modules.pop("app.config", None)

    def tearDown(self):
        """Teardown."""
        sys.modules.pop("app.config", None)

    @patch("app.MongoEngine")
    def test_db_auth(self, db):
        """Calling app.db_auth, the connection to the db should be opened."""
        with self.env:
            from app import app, db_auth
            from app.config import ProductionConfig
            app.config.from_object(ProductionConfig)
            app.testing = True
            with app.app_context():
                conf = app.config["MONGODB_SETTINGS"]
                db_auth()
                db.return_value.connection[
                    conf["host"].split("/")[-1] or conf["db"]
                ].authenticate.assert_called_once_with(
                    conf["username"], conf["password"]
                )

    @patch("app.MongoEngine")
    def test_db_auth_without_cred(self, db):
        """authenticate shouldn't be called if there's no db credentials."""
        from app import app, db_auth
        from app.config import DevelConfig
        app.config.from_object(DevelConfig)
        app.testing = True
        with app.app_context():
            conf = app.config["MONGODB_SETTINGS"]
            db_auth()
            db.return_value.connection[
                conf["host"].split("/")[-1] or conf["db"]
            ].authenticate.assert_not_called()
