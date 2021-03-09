
from SoftwareDev import settings
import logging

from django.template import loader, Context, Template

from os import environ as environ_variables
import pickle
from base64 import urlsafe_b64encode, urlsafe_b64decode, b64decode
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email import message_from_string

from googleapiclient.errors import HttpError
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

# boto is used *ONLY* in deployed app to access secrets
if True or ("DJANGO-AWS-4UMS-DEPLOYED" in environ_variables):
    import boto3
    from botocore.exceptions import ClientError


def create_message(sender, to, subject, message_html):
    """
    Create a message for an email.

    :param sender: Email address of the sender.
    :param to: Email address of the receiver.
    :param subject: The subject of the email message.
    :param message_html: Message contents as HTML.

    :returns:
        A base64 encoded email object.
    """
    message = MIMEText(message_text, "html")
    message['to'] = to
    message['from'] = sender
    message['subject'] = subject

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
    except HttpError as error:
        logger = logging.getLogger("root")
        logger.error(
            "HTTP error occured when calling the Gmail API:"
        )
        logger.error(str(error))


def build_email(email_addr, user_id, reset_code, first_name, username):
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

    template = loader.get_template("reset_email.html")

    context = {'username': username, 'first_name': first_name, 'url': link_url}


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
    #DEBUG: remove hard trap
    if False and ("DJANGO-AWS-4UMS-DEPLOYED" not in environ_variables):
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

    try:
        secret_value = client.get_secret_value(SecretId="4ums/email-creds")
    except ClientError as e:
        logger = logging.getLogger("root")
        if e.response['Error']['Code'] == 'ResourceNotFoundException':
            logger.error(
                "Failed to send email - Couldn't get secret '4ums/email-creds'"
            )
        elif e.response['Error']['Code'] == 'InvalidRequestException':
            logger.error(
                f"Failed to send email - secret request was invalid due to: {e}"
            )
        elif e.response['Error']['Code'] == 'InvalidParameterException':
            logger.error(
                f"Failed to send email - secret request had invalid params: {e}"
            )
        else:
            logger.error(
                "Failed to send email - secret request returned an error"
            )
        return

    creds_raw = b64decode(secret_value['SecretString'])
    creds = pickle.loads(creds_raw)

    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            #credentials not usable; can't send email
            logger = logging.getLogger("root")
            logger.error(
                "Failed to send email - Gmail API credentials are invalid"
            )

    service = build('gmail', 'v1', credentials=creds)
    send_message(service, "me", message)
