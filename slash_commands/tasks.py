# -*- coding: utf-8 -*-

import pickle
from slash_commands.celery import app

@app.task
def executor(func, *args, **kwargs):
    """ celery task to execute handler functions asynchronously """
    func(*args, **kwargs)
