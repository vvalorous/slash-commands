from celery import Celery


app = Celery(__name__)
app.conf.update(
    imports=["slash_commands.tasks"],
    accept_content=["pickle"],
    task_serializer="pickle",
    event_serializer="pickle",
    result_serializer="pickle"
)
