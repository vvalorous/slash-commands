# coding=utf-8

import subprocess

from .base import SlashCommand


class Systemctl(SlashCommand):
    """ Command to perform tasks associated with services """
    command = '/service'

    def handler(self):
        """ This method defines what needs to be done when this command is invoked  """
        command = self.payload['text']
        proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        return {'text': '\n'.join([x for x in proc.stdout])}
