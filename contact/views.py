'''
Conctact form views
'''

import json
import random
from smtplib import SMTPException
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import View
from django.conf import settings
from django.template import loader
from django.core.urlresolvers import reverse

from about.models import Developer
from common import gen_hash

from .models import VerifiedEmail, PendingVerification
from .forms import ContactForm, VerificationForm


class Contact(View):
    '''
    Contact Views.
    These views has 2 views, get method and post method.
    Get method is... as you know. post method is used when
    sending email
    '''
    template_name = "contact.html"
    form = ContactForm
    mail_text = loader.get_template("mail.txt")
    verification_mail_text = loader.get_template("verification_mail.txt")
    verification_mail_html = loader.get_template("verification_mail.html")

    def get(self, request, dev_hash=None):
        '''
        Returns contact view
        '''
        PendingVerification.remove_expired()
        # pylint: disable=unused-argument, no-member
        developers = [
            developer.to_dict() for developer in Developer.objects.all()
        ]
        # pylint: enable=no-member

        return render(
            request,
            self.template_name,
            {
                "developers": developers,
                "dev_hash": dev_hash,
                "issues_tracker": (
                    "https://github.com/hysoftware/hysoftware.net/issues"
                )
            }
        )

    def __verify_mail_field(self, request, dev_hash):
        '''
        Validate form fields
        '''
        payload = json.loads(request.body.decode("utf-8"))
        if not isinstance(dev_hash, str):
            return JsonResponse(
                {
                    "error": 404,
                    "backend": ["Which person you want to send message??"]
                },
                status=404
            )

        if dev_hash != payload.get("recipient_address"):
            return JsonResponse(
                {
                    "error": 404,
                    "backend": [(
                        "Payload address must be "
                        "the same as URL address"
                    )]
                },
                status=404
            )
        payload = self.form(payload)

        if not payload.is_valid():
            errors = dict(payload.errors)
            errors.update(
                {
                    "error": 417
                }
            )
            return JsonResponse(errors, status=417)
        payload = payload.clean()

        verified_email = request.session.get("verified_email")
        if not verified_email:
            return (False, payload)
        elif gen_hash(verified_email["recipient_email"]) == \
                payload["recipient_address"] and \
                verified_email["sender_email"] == \
                payload["sender_email"]:
            return (True, payload)

        request.session["verified_email"] = None
        return JsonResponse(
            {
                "error": 417,
                "backend": ["Your verification is invalid."]
            },
            status=404
        )

    def send_mail(self, session, data):
        '''
        Contact to hysoftware person
        '''
        try:
            send_mail(
                (
                    "Mail from hysoftware.net contact form -- {}"
                ).format(
                    data["sender_name"]
                ),
                self.mail_text.render({
                    "sender_name": data["sender_name"],
                    "message": data["message"]
                }),
                data["sender_email"],
                [session["verified_email"]["recipient_email"]]
            )
        except SMTPException:
            return JsonResponse(
                {
                    "error": 500,
                    "backend": ["SMTP Server seems to be down!!"]
                }, status=500
            )
        success_params = {
            "success": "Your message has been successfully sent!"
        }
        if settings.DEBUG:
            from django.core.mail import outbox
            message = outbox.pop()
            success_params.update(
                {
                    "additional_info": {
                        "subject": message.subject,
                        "body": message.body,
                        "from": message.from_email,
                        "to": message.to
                    }
                }
            )
        return JsonResponse(success_params)

    def __send_verification_mail(self, request, data):
        '''
        Send Verification Mail
        '''
        token = ("").join(
            [random.choice("abcdef0123456789") for counter in range(40)]
        )
        session = request.session
        # pylint: disable=no-member
        try:
            PendingVerification(
                email_hash=gen_hash(data["sender_email"]),
                name=data["sender_name"],
                assignee=Developer(email=session["recipient_email"]),
                message=data["message"]
            ).set_token(token).set_expiration().save()
        except TypeError:
            return JsonResponse(
                {
                    "error": 404,
                    "backend": ["Recipient not found"]
                }, status=404
            )
        # pylint: enable=no-member
        try:
            verification_context = {
                "name": data["sender_name"],
                "expire": int(
                    settings.CONTACT_VIRIFICATION_EXPIRES.seconds / 3600
                ),
                "url": request.build_absolute_uri(
                    reverse("verify_address", args=[token])
                )
            }
            send_mail(
                "Thanks for contacting hysoftware.net! but...",
                self.verification_mail_text.render(verification_context),
                "noreply@hysoftware.net",
                [data["sender_email"]],
                html_message=self.verification_mail_html.render(
                    verification_context
                )
            )
        except SMTPException:
            return JsonResponse(
                {
                    "error": 500,
                    "backend": ["SMTP Server seems to be down!!"]
                }, status=500
            )
        success_params = {
            "success": "Verification mail has been sent!"
        }
        if settings.DEBUG:
            from django.core.mail import outbox
            message = outbox.pop()
            success_params.update(
                {
                    "additional_info": {
                        "subject": message.subject,
                        "body": message.body,
                        "from": message.from_email,
                        "to": message.to
                    }
                }
            )
        return JsonResponse(success_params)

    def post(self, request, dev_hash=None):
        '''
        Send mail to the corresponding contact
        '''
        PendingVerification.remove_expired()
        data = self.__verify_mail_field(request, dev_hash)
        if isinstance(data, HttpResponse):
            return data
        else:
            if data[0] is False:
                return self.__send_verification_mail(request, data[1])
            else:
                return self.send_mail(request.session, data[1])


def check_email_in_list(request, dev_hash):
    '''
    Checks whether requested email is in developer's list
    '''
    developer = Developer.by_hash(dev_hash)
    request.session["verified_email"] = None

    if not developer:
        # We don't know such developer!
        return HttpResponse(status=404)

    request.session["recipient_email"] = developer.email

    # Check developer's list
    his_list = None
    try:
        his_list = VerifiedEmail.find_by_email(
            request.GET["sender"],
            developer.email
        )
    except MultiValueDictKeyError:
        # This error is only thrown when sender is null.
        return HttpResponse(status=404)

    if his_list and len(his_list) > 0:
        # He is listed on developer's list
        request.session["verified_email"] = {
            "sender_email": request.GET["sender"],
            "recipient_email": developer.email
        }
        return HttpResponse(status=200)
    return HttpResponse(status=404)


class AddressVerification(View):
    '''
    AddressVerification views
    '''
    # pylint: disable=too-few-public-methods

    template_file = "verify_mail.html"
    form = VerificationForm

    def get(self, request, token):
        '''
        Return verification view if the mail hash is found.
        Otherwise returns 404.

        Note: shows view even if the hash is not found when
            DEBUG mode
        '''

        PendingVerification.remove_expired()
        if settings.DEBUG:
            return render(request, self.template_file)

        get_object_or_404(
            PendingVerification,
            token_hash=gen_hash(token)
        )
        return render(
            request,
            self.template_file, {
                "issues_tracker": (
                    "https://github.com/hysoftware/hysoftware.net/issues"
                )
            }
        )

    def post(self, request, token):
        '''
        Verify Email
        '''
        pend = get_object_or_404(
            PendingVerification,
            token_hash=gen_hash(token)
        )
        payload = self.form(json.loads(request.body.decode("utf-8")))

        if not payload.is_valid():
            errors = dict(payload.errors)
            errors.update({"error": 417})
            return JsonResponse(errors, status=417)

        payload = payload.clean()
        verified_model = VerifiedEmail(
            email_hash=pend.email_hash,
            assignee=pend.assignee
        )
        verified_model.save()
        result = Contact().send_mail(
            {"verified_email": {"recipient_email": pend.assignee.email}},
            {
                "sender_name": pend.name,
                "sender_email": payload["email"],
                "message": pend.message
            }
        )
        pend.delete()
        return result
