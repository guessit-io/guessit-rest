#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser


def bootstrap(app, args=None):
    opts = ArgumentParser()

    opts.add_argument('-l', '--listening-adress', dest='listening_adress', default='0.0.0.0',
                      help='Listening IP Adress of the HTTP Server.')
    opts.add_argument('-p', '--listening-port', dest='listening_port', default=None, type=int,
                      help='Listening TCP Port of the HTTP Server.')

    parsed_opts = opts.parse_args(args)

    app.run(host=parsed_opts.listening_adress, port=parsed_opts.listening_port)
