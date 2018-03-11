# -*- coding: utf-8 -*-

import pickle
import importlib

from flask import request, Flask

from slash_commands.conf import settings
from slash_commands.tasks import executor
from slash_commands.handler import EventHandler

# define flask app
app = Flask(__name__)

# import all handlers
for module in settings.INSTALLED_HANDLERS:
    importlib.import_module(module)

# endpoint to dispatch event handler
@app.route("/events", methods=["POST"])
def events():

    # parse payload
    payload = request.get_json()
    print(payload)
    event = payload.get("type", "unknown").replace(".", "_")

    # invoke handlers
    handlers = EventHandler.get_handlers()
    for handler in handlers:
        event_handler = getattr(handler, event)
        if event_handler:
            executor.delay(event_handler, payload)

    # return 200 OK
    return "success"
