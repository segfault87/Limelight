# -*- coding: utf-8 -*-

from flask.ext.script import Manager
import .web


def create_app(config_path):
    return web.create_app(config_path)


manager = Manager(create_app)
manager.add_option('-c', '--config', default='conf/default.yml',
                   dest='config_path')


manager.run()


