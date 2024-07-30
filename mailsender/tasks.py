import logging
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
from .models import SpamServis, MailingAttempt

logger = logging.getLogger(__name__)

scheduler = BackgroundScheduler()


def start_scheduler():
    if not scheduler.running:
        scheduler.add_job(
            send_mailing,
            IntervalTrigger(minutes=1),
            id='send_mailing',
            name='Send mailing every 1 minute',
            replace_existing=True
        )
        scheduler.start()
    else:
        logger.info("Scheduler is already running.")


def send_mailing():
    logger.debug("send_mailing task is running")
    now = timezone.now()
    mailings = SpamServis.objects.filter(first_send_date__lte=now, status='started')

    for mailing in mailings:
        try:
            message = mailing.message
            clients = mailing.clients.all()
            for client in clients:
                send_mail(
                    message.title,
                    message.body,
                    settings.DEFAULT_FROM_EMAIL,
                    [client.email],
                    fail_silently=False,
                )
            logger.debug(f"Mailing {mailing.id} sent successfully")
            MailingAttempt.objects.create(
                mailing=mailing,
                status='success',
                server_response='Mail sent successfully'
            )
        except Exception as e:
            logger.error(f"Failed to send mailing {mailing.id}: {e}")
            MailingAttempt.objects.create(
                mailing=mailing,
                status='failure',
                server_response=str(e)
            )