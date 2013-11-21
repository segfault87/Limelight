# -*- coding: utf-8 -*-

from gevent.monkey import patch_all

from limelight.web import application


# gevent monkeypatch
patch_all()

