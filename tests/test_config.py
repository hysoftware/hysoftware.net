#!/usr/bin/env python
# coding=utf-8

"""Setting test."""

from unittest.mock import patch

from django.test import TestCase


class ProductionConfigTest(TestCase):
    """Production Configuration Test."""

    def setUp(self):
        """Setup."""
        self.allowed_hosts = [
            "allowed.io",
            "allowed2.io",
            "allowed3.io",
            "allowed4.io",
            ""
        ]
        self.environ = {
            "SECRET": "test",
            "RECAPTCHA_PUBLIC_KEY": "recaptcha_test_pubkey",
            "RECAPTCHA_PRIVATE_KEY": "recaptcha_test_privkey",
            "MAILGUN_KEY": "mailgun-key",
            "MAILGUN_URL": "mailgun-url",
            "ALLOWED_HOSTS": (
                "allowed.io, allowed2.io,allowed3.io, allowed4.io,"
            ),
            "CELERY_BROKER_URL": "test_broker",
            "DB_ENGINE": "test_db_engine",
            "DB_NAME": "test_db_name",
            "DB_USER": "test_db_user",
            "DB_PW": "test_db_pw",
            "DB_HOST": "test_db_host",
            "DB_PORT": "test_db_port",
            "SQS_REGION": "us-east-1a",
            "SQS_PREFIX": "test",
            "AWS_ACCESS_KEY_ID": "dGVzdGFwaWtleQo=",
            "AWS_SECRET_ACCESS_KEY": "dGVzdGFwaXNlY3JldAo=",
            "AWS_STORAGE_BUCKET_NAME": "test_bucket"
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

    def test_allowed_hosts(self):
        """Allowed host test."""
        self.assertNotEqual(
            self.conf_p.ALLOWED_HOSTS,
            self.conf_d.ALLOWED_HOSTS
        )
        self.assertEqual(
            self.conf_p.ALLOWED_HOSTS,
            self.allowed_hosts
        )

    def test_celery_broker(self):
        """Celery broker should be differ from devel env."""
        self.assertNotEqual(
            self.conf_p.CELERY_BROKER_URL,
            self.conf_d.CELERY_BROKER_URL
        )
        self.assertEqual(
            self.conf_p.CELERY_BROKER_URL,
            self.environ["CELERY_BROKER_URL"]
        )

    def test_db(self):
        """Database URL should be differ from devel."""
        self.assertNotEqual(self.conf_p.DATABASES, self.conf_d.DATABASES)
        self.assertDictEqual({
            "default": {
                "ENGINE": self.environ["DB_ENGINE"],
                "NAME": self.environ["DB_NAME"],
                "USER": self.environ["DB_USER"],
                "PASSWORD": self.environ["DB_PW"],
                "HOST": self.environ["DB_HOST"],
                "PORT": self.environ["DB_PORT"]
            }
        }, self.conf_p.DATABASES)

    def test_sqs(self):
        """SQS related settings should be there!."""
        self.assertDictEqual({
            "region": self.environ["SQS_REGION"],
            "queue_name_prefix": self.environ["SQS_PREFIX"]
        }, self.conf_p.CELERY_BROKER_TRANSPORT_OPTIONS)

    def test_aws_storage(self):
        """The storage should be S3."""
        self.assertIn("storages", self.conf_p.THIRD_PARTY_APPS)
        self.assertEqual(
            self.conf_p.DEFAULT_FILE_STORAGE,
            "storages.backends.s3boto3.S3Boto3Storage"
        )
        self.assertEqual(
            self.conf_p.STATICFILES_STORAGE, self.conf_d.STATICFILES_STORAGE
        )
        self.assertEqual(
            self.conf_p.AWS_ACCESS_KEY_ID,
            self.environ["AWS_ACCESS_KEY_ID"]
        )
        self.assertEqual(
            self.conf_p.AWS_SECRET_ACCESS_KEY,
            self.environ["AWS_SECRET_ACCESS_KEY"]
        )
        self.assertEqual(
            self.conf_p.AWS_STORAGE_BUCKET_NAME,
            self.environ["AWS_STORAGE_BUCKET_NAME"]
        )
