'''
Conctact form views
'''

import json
from smtplib import SMTPException
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import HttpResponse, JsonResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.utils import timezone
from django.views.generic import View
from django.conf import settings
from django.template import Context, loader
from django.core.urlresolvers import reverse

from about.models import Developer
from common import gen_hash

from .models import VerifiedEmail, PendingVerification
from .forms import ContactForm


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
                "dev_hash": dev_hash
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
                    "message": "Which person you want to send message??"
                },
                status=404
            )

        if dev_hash != payload.get("recipient_address"):
            return JsonResponse(
                {
                    "error": 404,
                    "message": (
                        "Payload address must be "
                        "the same as URL address"
                    )
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
        print(payload)

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
                "message": "Your verification is invalid."
            },
            status=404
        )

    def send_mail(self, session, data):
        '''
        Contact to hysoftware person
        '''
        try:
            context = Context(
                {
                    "sender_name": data["sender_name"],
                    "message": data["message"]
                }
            )
            send_mail(
                (
                    "Mail from hysoftware.net contact form -- {}"
                ).format(
                    data["sender_name"]
                ),
                self.mail_text.render(context),
                data["sender_email"],
                [session["verified_email"]["recipient_email"]]
            )
        except SMTPException:
            return JsonResponse(
                {
                    "error": 500,
                    "message": "SMTP Server seems to be down!!"
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

    def __send_verification_mail(self, session, data):
        '''
        Send Verification Mail
        '''
        mail_hash = gen_hash(data["sender_email"])
        expire = timezone.now() +\
            settings.CONTACT_VIRIFICATION_EXPIRES
        # pylint: disable=no-member
        try:
            PendingVerification(
                email_hash=mail_hash,
                name=data["sender_name"],
                assignee=Developer(email=session["recipient_email"]),
                message=data["message"],
                expires=expire
            ).save()
        except TypeError:
            return JsonResponse(
                {
                    "error": 404,
                    "message": "Recipient not found"
                }, status=404
            )
        # pylint: enable=no-member
        verification_context = Context(
            {
                "name": data["sender_name"],
                "url": reverse("verify_address", args=[mail_hash])
            }
        )
        try:
            send_mail(
                "Thanks for contacting hysoftware.net person! but...",
                self.verification_mail_text.render(
                    verification_context
                ),
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
                    "message": "SMTP Server seems to be down!!"
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
                return self.__send_verification_mail(request.session, data[1])
            else:
                return self.send_mail(request.session, data[1])


def check_email_in_list(request, dev_hash):
    '''
    Checks whether requested email is in developer's list
    '''
    developer = Developer.by_hash(dev_hash)
    request.session["verified_email"] = None
    request.session["recipient_email"] = developer.email

    if not developer:
        # We don't know such developer!
        return HttpResponse(status=404)

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

    def get(self, request, mail_hash):
        '''
        Return verification view if the mail hash is found.
        Otherwise returns 404.

        Note: shows view even if the hash is not found, when
            DEBUG mode
        '''

        PendingVerification.remove_expired()
        if settings.DEBUG:
            return render(request, self.template_file)

        get_object_or_404(
            PendingVerification,
            email_hash=mail_hash
        )
        return render(request, self.template_file)
