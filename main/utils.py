import logging

from django.core.handlers.wsgi import WSGIRequest
from django.core.mail import EmailMessage
from django.template import loader
from django.urls import reverse

from main.models import CourseData, Email, FeedbackData


def send_email_notification(title: str, body: str, to: list) -> None:
    try:
        email = EmailMessage(title, body=body, to=to)
        email.content_subtype = 'html'
        email.send()
    except Exception as e:
        logging.error('There was error when sending notification to email')


def get_email_list() -> list:
    email_list = (
        Email.objects.values_list('email', flat=True).filter(is_active=True)
    )
    return email_list


def prepare_course_data_text_and_notify(request: WSGIRequest, course_data: CourseData) -> None:
    short_url = reverse('admin:main_coursedata_change', args=(course_data.id,))
    link = request.build_absolute_uri(short_url)
    title = 'Новый запись!'
    template = loader.get_template('partials/email_text.html')
    text = template.render(context=dict(title=title, link=link))
    send_email_notification(title, text, get_email_list())


def prepare_feedback_data_text_and_notify(request: WSGIRequest, feedback_data: FeedbackData) -> None:
    short_url = reverse('admin:main_feedbackdata_change', args=(feedback_data.id,))
    link = request.build_absolute_uri(short_url)
    title = 'Новая заявка!'
    template = loader.get_template('partials/email_text.html')
    text = template.render(context=dict(title=title, link=link))
    send_email_notification(title, text, get_email_list())
