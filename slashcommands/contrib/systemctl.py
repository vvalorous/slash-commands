# coding=utf-8

import subprocess

from .base import SlashCommand


class Systemctl(SlashCommand):
    """ Command to perform tasks associated with services """
    command = '/systemctl'

    def handler(self):
        """ This method defines what needs to be done when this command is invoked  """
        command = self.payload['text']
        proc = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        return {'text': '\n'.join([str(x) for x in proc.stdout])}
