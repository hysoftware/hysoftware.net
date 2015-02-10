'''
Contact form admin model
'''

# pylint: disable=too-few-public-methods

from django.contrib import admin
from .models import (VerifiedEmails,
                     PendingVerification)


admin.site.register(VerifiedEmails)


@admin.register(PendingVerification)
class PendingVerificationAdmin(admin.ModelAdmin):
    '''
    Verification Pending Administration Form
    '''
    fieldsets = [
        ("Email and Token", {"fields": ["email_hash", "token"]}),
        ("Body", {"fields": ["message"]}),
        ("Expiration Date", {"fields": ["expires"]}),
    ]
