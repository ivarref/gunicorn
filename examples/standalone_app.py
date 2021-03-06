#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# An example of a standalone application using the internal API of Gunicorn.
#
#   $ python standalone_app.py
#
# This file is part of gunicorn released under the MIT license.
# See the NOTICE for more information.

from __future__ import unicode_literals

import multiprocessing
import random
import sys
import time
import uuid

import gunicorn.app.base
from gunicorn.six import iteritems

def number_of_workers():
    return (multiprocessing.cpu_count() * 2) + 1

resp = str(uuid.uuid4())

def handler_app(environ, start_response):
    response_body = b'Works fine'
    status = '200 OK'

    response_headers = [
        ('Content-Type', 'text/plain'),
    ]

    start_response(status, response_headers)
    sys.stdout.write('handling request ...\n')
    sys.stdout.flush()
    time.sleep(0.1 * random.random()) # do some work

    global resp
    return [resp]


class StandaloneApplication(gunicorn.app.base.BaseApplication):

    def __init__(self, app, options=None):
        self.options = options or {}
        self.application = app
        super(StandaloneApplication, self).__init__()

    def load_config(self):
        config = dict([(key, value) for key, value in iteritems(self.options)
                       if key in self.cfg.settings and value is not None])
        for key, value in iteritems(config):
            self.cfg.set(key.lower(), value)

    def load(self):
        return self.application


if __name__ == '__main__':
    options = {
        'bind': '%s:%s' % ('0.0.0.0', '8080'),
        'workers': 1,
    }
    StandaloneApplication(handler_app, options).run()
