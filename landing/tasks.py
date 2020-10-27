from django.core.mail import send_mail
from .models import Contact
from kdf.celery import app
from django.conf import settings


@app.task
def send_email_task(contact_id):
    try:
        contact = Contact.objects.get(id=contact_id)
        mail_sent = send_mail(subject=contact.message_title,
                              message=contact.message_text,
                              from_email='admin@mg.researchershubs.live',
                              recipient_list=[contact.sender_email, settings.MAIN_ADMINISTRATOR_EMAIL])
    except Contact.DoesNotExist:
        return False

    return mail_sent
