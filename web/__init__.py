# -*- coding: utf-8 -*-

from flask import Flask


application = Flask('Limelight')


@application.route('/')
def hello():
    return 'world'

