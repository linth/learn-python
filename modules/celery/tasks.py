from celery import Celery

# app = Celery('tasks', broker='redis://localhost:6379')
#
# @app.task
# def send_mail(email):
#     print("send mail to ", email)
#     import time
#     time.sleep(5)
#     return "success"
