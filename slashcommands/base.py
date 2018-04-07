# coding=utf-8

import requests


class SlashCommand(object):
    """ This class represent the structure or layout of a command """

    def __init__(self, payload):
        """
        This method initializes the command instance

        Args:
            payload (dict) -- payload sent from slack
        """
        self.payload = payload

    @property
    def command(self):
        """ pattern used to invoke the command """
        raise NotImplementedError()

    def pre_execution_hook(self):
        """ This method is invoked before calling the handler of the command """
        pass

    def handler(self):
        """ logic or intelligence of the command """
        pass

    def post_execution_hook(self):
        """ This method is invoked after calling the handler of the command """
        pass

    def send_response(self, response):
        """
        This method send response back to the slack

        Args:
            response (dict) -- dictionary containing the response
        """
        response.update({'response_type': 'in_channel'})
        endpoint = self.payload['response_url']
        ack = requests.post(endpoint, json=response)
        ack.raise_for_status()

    def execute(self):
        """ This method executed the command along with the pre and post hooks """
        self.pre_execution_hook()
        response = self.handler()
        self.post_execution_hook()
        self.send_response(response)
