# -*- coding: utf-8 -*-

import requests


class Command(object):
    """ base class for slash command """

    def __init__(self, payload):
        """ initialize class """
        self.response = {}
        self.payload = payload
        for key, val in payload.items():
            setattr(self, key, val)

    def execute(self):
        """ implementation of command """
        raise NotImplemented

    def reply(self):
        """ apply token and send reply to slack """
        self.response.update({"token": self.token})
        response = requests.post(self.response_url, self.response)
        print(response.content)

    @classmethod
    def get_commands(cls):
        """ get all subclasses """
        return cls.__subclasses__()
