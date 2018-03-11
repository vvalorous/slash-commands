# -*- coding: utf-8 -*-

import pickle
import importlib

from flask import request, Flask

from slash_commands.conf import settings
from slash_commands.tasks import executor
from slash_commands.command import Command

# define flask app
app = Flask(__name__)

# import all handlers
for module in settings.INSTALLED_HANDLERS:
    importlib.import_module(module)

# endpoint to dispatch event handler
@app.route("/", methods=["POST"])
def api():

    # parse data
    command = request.form.get("command")

    # invoke handlers
    command_handlers = Command.get_commands()
    for handler in command_handlers:
        if handler.command == command:
            executor.delay(handler, request.form)

    # return 200 OK
    return "success"
