# -*- coding: utf-8 -*-


class EventHandler(object):
    """ base class for all event handlers """

    @classmethod
    def get_handlers(cls):
        """ get all subclasses of e()vent handler """
        return cls.__subclasses__()
