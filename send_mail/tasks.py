from main.celery import app

from .utils import send

@app.task
def send_some_email(user_mail,yt_link):
    send(user_mail,yt_link)