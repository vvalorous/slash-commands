# -*- coding: utf-8 -*-

from slash_commands.handler import EventHandler


class MessageHandler(EventHandler):

    @staticmethod
    def message(payload):
        print(payload)
