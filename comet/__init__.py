# -*- coding: utf-8 -*-


class EventGenerator(type):
    def __new__(meta, name, bases, dct):
        cls = super(EventGenerator, meta).__new__(meta, name, bases, dct)
        if not hasattr(cls, '__fields__'):
            raise TypeError('No fields attribute')
        return cls


class Event(object):
    __metaclass__ = EventGenerator
