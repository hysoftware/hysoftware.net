'''
Contact Forms
'''

from django import forms


# pylint: disable=too-few-public-methods
class ContactForm(forms.Form):
    '''
    Contact Form
    '''
    sender_name = forms.CharField(required=True)
    sender_email = forms.EmailField(required=True)
    recipient_address = forms.CharField(required=True)
    message = forms.CharField(required=True)

    def __str__(self):
        return (
            "ContactForm -- From: {} <{}>, To {}, message:\n"
            "{}\n"
        ).format(
            self.sender_name,
            self.sender_email,
            self.recipient_address,
            self.message
        )

    __unicode__ = __str__
# pylint: enable=too-few-public-methods
