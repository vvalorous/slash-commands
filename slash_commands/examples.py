# -*- coding: utf-8 -*-

from slash_commands.command import Command


class Systemctl(Command):
    """ slash command - /systemctl """
    command = "/systemctl"

    @staticmethod
    def execute(payload):
        print(payload)
