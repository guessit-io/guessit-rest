#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import guessit

from flask import url_for


class TestVersion(object):
    def test_version(self, client):
        response = client.get(url_for('.guessitversion'))
        assert response.status_code == 200
        assert 'version' in response.json
        assert response.json['version'] == guessit.__version__


class AbstractTestGuessit(object):
    def request(self, client, data=None):  # pragma:no cover
        raise NotImplementedError

    def test_language(self, client):
        response = self.request(client, {'filename': 'test-FRENCH.avi'})
        assert response.status_code == 200
        assert 'title' in response.json
        assert 'language' in response.json
        assert response.json['title'] == 'test'
        assert response.json['language'] == 'French'

    def test_single(self, client):
        response = self.request(client, {'filename': 'test.avi'})
        assert response.status_code == 200
        assert 'title' in response.json
        assert response.json['title'] == 'test'

    def test_no_filename(self, client):
        response = self.request(client)
        assert response.status_code == 400
        assert 'message' in response.json
        assert 'filename' in response.json['message']
        assert 'Missing' in response.json['message']['filename']


class TestGuessitGet(AbstractTestGuessit):
    def request(self, client, data=None):
        return client.get(url_for('.guessit'), query_string=data)


class TestGuessitPost(AbstractTestGuessit):
    def request(self, client, data=None):
        return client.post(url_for('.guessit'), content_type="application/json", data=json.dumps(data))

