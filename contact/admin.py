'''
Contact form admin model
'''

# pylint: disable=too-few-public-methods

from django.contrib import admin
from .models import (VerifiedEmail,
                     PendingVerification)


admin.site.register(VerifiedEmail)


@admin.register(PendingVerification)
class PendingVerificationAdmin(admin.ModelAdmin):
    '''
    Verification Pending Administration Form
    '''
    fieldsets = [
        (
            "Email, Token hash, and recipient",
            {
                "fields": [
                    "email_hash",
                    "token_hash",
                    "assignee"
                ]
            }
        ),
        ("Body", {"fields": ["message"]}),
        ("Expiration Date", {"fields": ["expires"]}),
    ]
