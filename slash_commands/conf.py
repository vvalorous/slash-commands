# -*- coding: utf-8 -*-

import os
from importlib import import_module

# default settings file
settings = import_module('slash_commands.settings')

# external settings file
settings_file = os.getenv("SLASH_COMMANDS_SETTINGS")
if settings_file:
    settings = import_module(settings_file)
