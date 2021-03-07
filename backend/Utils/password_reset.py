
from SoftwareDev import settings
import logging

from django.template import loader, Context, Template

from os import environ as environ_variables
import pickle
from base64 import urlsafe_b64encode, urlsafe_b64decode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import message_from_string

from googleapiclient.errors import HttpError

# boto is used *ONLY* in deployed app to access secrets
if "DJANGO-AWS-4UMS-DEPLOYED" in environ_variables:
    import boto3


def create_message(sender, to, subject, message_text, message_html):
    """
    Create a message for an email.

    :param sender: Email address of the sender.
    :param to: Email address of the receiver.
    :param subject: The subject of the email message.
    :param message_text: Message contents as raw text.
    :param message_html: Message contents as HTML.

    :returns:
        A base64 encoded email object.
    """
    message = MIMEMultipart('alternative')
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

    message.attach(MIMEText(message_text, "plain"))
    message.attach(MIMEText(message_html, "html"))

    return {'raw': urlsafe_b64encode(message.as_string().encode()).decode()}


def send_message(service, user_id, message):
    """
    Send an email message.

    :param service: Authorized Gmail API service instance.
    :param user_id: User's email address. The special value "me"
                    can be used to indicate the authenticated user.
    :param message: base64 encoded message to be sent.
    """
    try:
        message = (service.users().messages().send(
            userId=user_id, body=message
        ).execute())
        logger = logging.getLogger(__name__)
        logger.error(
            "HTTP error occured when attempting to call the Gmail API"
        )
    except HttpError as error:
        logger = logging.getLogger(__name__)
        logger.error(
            "HTTP error occured when attempting to call the Gmail API"
        )
        logger.error(str(error))


def build_password_reset_email(email_addr, user_id, reset_code, first_name, username):
    """
    Build the password reset email.

    :param email_addr: email address of the user having their password reset.
    :param user_id:    ID of the user.
    :param reset_code: code used to validate the reset.
    :param first_name: First name of the user.
    :param username:   username of the user.

    :return:
        A base64 encoded email object.
    """

    link_url = f"http://4ums.co.uk/login/passwordreset?id={user_id}&code={reset_code}"

    plain_template = loader.get_template("plain_email.txt")
    html_template = loader.get_template("html_email.html")

    context = Context(
        {'username': username, 'first_name': first_name, 'url': link_url}
    )

    plain_str = plain_template.render(context)
    html_str = html_template.render(context)

    message = create_message(
        "me", email_addr, "Password reset", plain_str, html_str
    )

    return message


def send_reset_email(message):
    """
    Send the reset email.

    :param message: base64 encoded message object
    """

    if "DJANGO-AWS-4UMS-DEPLOYED" not in environ_variables:
        # don't send the email unless we're in live deployment

        # for testing purposes: decode plain text and print to console
        msg_b64 = message['raw']
        msg_str = urlsafe_b64decode(msg_b64.encode()).decode()

        message = message_from_string(msg_str)
        for payload in message.get_payload():
            if payload.get_content_type() == "text/plain":
                print(payload.get_payload())
                break
        return

    session = boto3.session.Session()
    client = session.client(
        service_name="secretsmanager", region_name="us-west-2"
    )
    creds_secret = client.get_secret_value(SecretId="4ums/email-creds")
    creds_raw = creds_secret['SecretString']

    #process email creds here
