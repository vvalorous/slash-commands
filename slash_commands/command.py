# -*- coding: utf-8 -*-

import json
import requests


class Command(object):
    """ base class """

    @classmethod
    def get_commands(cls):
        """ fetch all commands """
        return cls.__subclasses__()

    def __init__(self, payload):
        """ initialize class """
        self.response = {}
        self.payload = payload
        for key, val in payload.items():
            setattr(self, key, val)

    def execute(self):
        """ implementation of command """
        raise NotImplemented

    @property
    def headers(self):
        """ response headers """
        return {"response_headers": "application/json"}

    def reply(self):
        """ apply token and send reply to slack """
        self.response.update({"token": self.token})
        requests.post(self.response_url, data=self.response, headers=self.headers)
