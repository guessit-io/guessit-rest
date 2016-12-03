#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

import guessit
from flask import url_for
from werkzeug.datastructures import MultiDict

import guessitrest


class TestVersion(object):
    def test_version(self, client):
        response = client.get(url_for('.guessitversion'))
        assert response.status_code == 200
        assert 'guessit' in response.json
        assert guessit.__version__ == response.json['guessit']
        assert 'rest' in response.json
        assert guessitrest.__version__ == response.json['rest']


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
        assert 'Filename to parse' in response.json['message']['filename']


class TestGuessitGet(AbstractTestGuessit):
    def request(self, client, data=None):
        return client.get(url_for('.guessit'), query_string=data)


class TestGuessitPost(AbstractTestGuessit):
    def request(self, client, data=None):
        return client.post(url_for('.guessit'), content_type="application/json", data=json.dumps(data))


class AbstractTestGuessitList(object):
    def request(self, client, data=None):  # pragma:no cover
        raise NotImplementedError

    def test_single(self, client):
        response = self.request(client, {'filename': 'test-FRENCH.avi'})
        assert response.status_code == 200
        assert len(response.json) == 1
        assert 'title' in response.json[0]
        assert response.json[0]['title'] == 'test'

    def _build_multiple_data(self):
        pass

    def test_multiple(self, client):
        response = self.request(client, self._build_multiple_data())
        assert response.status_code == 200
        assert len(response.json) == 3
        assert 'title' in response.json[0]
        assert response.json[0]['title'] == 'test'
        assert 'title' in response.json[1]
        assert response.json[1]['title'] == 'test2'
        assert 'title' in response.json[2]
        assert response.json[2]['title'] == 'test3'

    def test_no_filename(self, client):
        response = self.request(client)
        assert response.status_code == 400
        assert 'message' in response.json
        assert 'filename' in response.json['message']
        assert 'Filename to parse' in response.json['message']['filename']


class TestGuessitBatchGet(AbstractTestGuessitList):
    def _build_multiple_data(self):
        return MultiDict([('filename', 'test.avi'),
                          ('filename', 'test2.avi'),
                          ('filename', 'test3.avi')])

    def request(self, client, data=None):
        return client.get(url_for('.guessitlist'), query_string=data)


class TestGuessitBatchPost(AbstractTestGuessitList):
    def _build_multiple_data(self):
        return {'filename': ['test.avi', 'test2.avi', 'test3.avi']}

    def request(self, client, data=None):
        return client.post(url_for('.guessitlist'), content_type="application/json", data=json.dumps(data))
