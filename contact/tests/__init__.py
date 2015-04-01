'''
Contact testing module
'''

from .backend import (
    VerificationPendingExpirationTest,
    VerifiedEmailTests
)

__all__ = [
    "VerificationPendingExpirationTest",
    "VerifiedEmailTests"
]
