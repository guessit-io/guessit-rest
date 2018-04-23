#!/usr/bin/env python
# -*- coding: utf-8 -*-

from guessitrest.bootstrap import bootstrap


class TestBootstrap(object):
    def test_bootstrap(self, mocker):
        app = mocker.MagicMock()
        bootstrap(app, ["-l", "192.168.0.1", "-p", "3333"])
        app.run.assert_called_with(host='192.168.0.1', port=3333)
