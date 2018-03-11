# -*- coding: utf-8 -*-

from slash_commands.handler import Command


class Systemctl(Command):
    """ slash command - /systemctl """
    command = "/systemctl"

    @staticmethod
    def execute(payload):
        print(payload)
