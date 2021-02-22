from flask_mail import Message
from flask import current_app, Flask
from threading import Thread

from config.extensions import mail
from config import variables


def send_async_email(app: Flask, msg: str) -> None:
    with app.app_context():
        mail.send(msg)


def send_email(to: str, subject: str, body: str) -> None:
    app = current_app._get_current_object()

    msg = Message(
        subject,
        sender=variables.MAIL_USERNAME,
        recipients=[to]
    )
    msg.body = body

    thr = Thread(target=send_async_email, args=[app, msg])
    thr.start()
