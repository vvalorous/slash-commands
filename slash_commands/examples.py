# -*- coding: utf-8 -*-

import os

from slash_commands.command import Command


class Systemctl(Command):
    """ slash command - /systemctl """
    command = "/systemctl"

    def execute(self):
        date = os.popen("date").read()
        self.response.update({"text": date})
