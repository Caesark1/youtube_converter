from __future__ import unicode_literals 
from django.core.mail import send_mail
import youtube_dl



def send(user_mail,yt_link):
    ydl_opts = {
    'format': 'bestaudio',
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(
            yt_link, download=False)
        link_of_video = info['formats'][0]['url']    

    send_mail(
    'Hi',
    link_of_video,
    'kebec2015@example.com',
    [user_mail],
    fail_silently=False,)
