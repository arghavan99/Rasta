from celery.decorators import task
from celery.utils.log import get_task_logger

from apps.newsletter.send_mail import send_mail_to_subscribers

logger = get_task_logger(__name__)


@task(name="send_mail_to_subscriber_task")
def send_mail_to_subscribers_task(context, subject):
    return send_mail_to_subscribers(context, subject)

