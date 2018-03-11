# -*- coding: utf-8 -*-

from slash_commands.command import Command


class Systemctl(Command):
    """ slash command - /systemctl """
    command = "/systemctl"

    def execute(self):
        print(self.payload)
        self.response.update({"text": "Akhil@123"})
