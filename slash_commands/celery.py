# -*- coding: utf-8 -*-
from celery import Celery

# define celery app
app = Celery(__name__)

# update celery config to use pickle instead of json
app.conf.update(
    task_serializer="pickle",
    event_serializer="pickle",
    result_serializer="pickle",
    accept_content=["pickle"],
    imports=["slash_commands.tasks"],
)
