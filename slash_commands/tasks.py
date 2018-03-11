# -*- coding: utf-8 -*-

import pickle
from slash_commands.celery import app

@app.task
def executor(command, *args, **kwargs):
    """ celery task to execute handler functions asynchronously """
    command = command(*args, **kwargs)
    command.execute()
    command.reply()
