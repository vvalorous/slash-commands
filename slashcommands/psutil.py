# coding=utf-8

import psutil

from .base import SlashCommand


class PSUtil(SlashCommand):
    """ Command to perform tasks associated with processes """
    command = '/psutil'

    def handler(self):
        """ This method defines what needs to be done when this command is invoked  """
        pass
