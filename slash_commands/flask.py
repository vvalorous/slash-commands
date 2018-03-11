# -*- coding: utf-8 -*-

import pickle
import importlib

from flask import Flask, request

from slash_commands.conf import settings
from slash_commands.tasks import executor
from slash_commands.handler import EventHandler

app = Flask(__name__)

for module in settings.INSTALLED_HANDLERS:
    importlib.import_module(module)

@app.route("/events", methods=["POST"])
def events():

    # parse payload
    payload = request.get_json()
    event = payload.get("type", "unknown").replace(".", "_")

    # invoke handlers
    handlers = EventHandler.get_handlers()
    for handler in handlers:
        event_handler = getattr(handler, event)
        if event_handler:
            # event_handler = pickle.dumps(event_handler)
            executor.delay(event_handler, payload)

    # return 200 OK
    return "success"
