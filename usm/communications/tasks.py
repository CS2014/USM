import celery
from django.core.mail import send_mail, BadHeaderError

@celery.task
def send_sms_task(members, message_text):
    client = TwilioRestClient(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_ACCOUNT_AUTH_TOKEN)
    
    for member in members:
        if member.phone_number != None and member.phone_number != "":
            try:
                message = client.messages.create(
                    body=message_text,  # Message body, if any
                    to=member.phone_number.replace('-', ''),
                    _from=settings.TWILIO_ACCOUNT_PHONE
                )
                print message.sid
            except:
                print "MESSAGE ERRZ"
@celery.task
def send_email_task(members, message_subject, message_text):
    for member in members:
        try:
            send_mail(message_subject, message_text, 'no-reply@mysociety.github.io', [member.email])
        except:
            pass