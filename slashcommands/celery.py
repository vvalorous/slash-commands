# coding=utf-8

import os

from celery import Celery

os.environ.setdefault('SLASHCOMMANDS_BROKER', 'redis://localhost:6379/0')

broker = os.getenv('SLASHCOMMANDS_BROKER')

app = Celery('slashcommands', broker=broker)
app.conf.update({
    'accept_content': ['pickle'],
    'task_serializer': 'pickle',
    'event_serializer': 'pickle',
    'result_serializer': 'pickle',
})

@app.task
def process_request(instance):
    """ execute the slashcommand asynchronously """
    instance.execute()
