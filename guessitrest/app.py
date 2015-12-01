#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import json
import logging
from logging.handlers import RotatingFileHandler

from flask import Flask, make_response
from flask_restful import Api, Resource, reqparse

import guessit
from guessit.jsonutils import GuessitEncoder

app = Flask(__name__)
api = Api(app)
app.debug = os.environ.get('GUESSIT-REST-DEBUG', False)

if not app.debug:
    handler = RotatingFileHandler('guessit-rest.log', maxBytes=5*1024*1024, backupCount=5)
    handler.setLevel(logging.DEBUG)
    app.logger.addHandler(handler)


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = make_response(json.dumps(data, cls=GuessitEncoder, ensure_ascii=False), code)
    resp.headers.extend(headers or {})
    return resp


class GuessIt(Resource):
    def _impl(self, location):
        options = {}

        parser = reqparse.RequestParser()
        parser.add_argument('filename', action='store', required=True, help='Filename to parse', location=location)
        parser.add_argument('options', action='store', help='Guessit options', location=location)
        args = parser.parse_args()

        return guessit.guessit(args.filename, options)

    def get(self):
        """
        @api {get} /guessit guessit
        @apiName GuessItGet
        @apiGroup GuessIt

        @apiDescription Extracts as much information as possible from a video filename.

        @apiParam {String} filename Video filename on which to extract information.

        @apiParam {String} [options] Options to pass.

        @apiError {Object} message An object describing the error.

        @apiSuccess {Object} result Object containing all detected properties.

        @apiExample {curl} Example usage:
        curl "https://api.guessit.io/v2/guessit?filename=House.of.Cards.2013.S02E03.1080p.NF.WEBRip.DD5.1.x264-NTb.mkv"

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
              "title": "House of Cards",
              "year": 2013,
              "season": 2,
              "episode": 3,
              "screen_size": "1080p",
              "other": "Netflix",
              "format": "WEBRip",
              "audio_codec": "DolbyDigital",
              "audio_channels": "5.1",
              "video_codec": "h264",
              "release_group": "NTb",
              "container": "mkv",
              "mimetype": "video/x-matroska",
              "type": "episode"
            }
        """
        return self._impl('args')

    def post(self):
        """
        @api {get} /guessit guessit
        @apiName GuessItPost
        @apiGroup GuessIt

        @apiDescription Extracts as much information as possible from a video filename.

        @apiParam {String} filename Video filename on which to extract information.

        @apiParam {String} [options] Options to pass.

        @apiError {Object} message An object describing the error.

        @apiSuccess {Object} result Object containing all detected properties.

        @apiExample {curl} Example usage:
        curl -H "Content-Type: application/json" -X POST \
        -d '{"filename":"House.of.Cards.2013.S02E03.1080p.NF.WEBRip.DD5.1.x264-NTb.mkv"}' \
        https://api.guessit.io/v2/guessit

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
              "title": "House of Cards",
              "year": 2013,
              "season": 2,
              "episode": 3,
              "screen_size": "1080p",
              "other": "Netflix",
              "format": "WEBRip",
              "audio_codec": "DolbyDigital",
              "audio_channels": "5.1",
              "video_codec": "h264",
              "release_group": "NTb",
              "container": "mkv",
              "mimetype": "video/x-matroska",
              "type": "episode"
            }
        """
        return self._impl('json')


class GuessItVersion(Resource):
    def get(self):
        """
        @api {get} /guessit/version guessit/version
        @apiName GuessItVersion
        @apiGroup GuessIt

        @apiDescription Retrieves the version of guessit used by the API.

        @apiExample {curl} Example usage:
        curl "https://api.guessit.io/v2/guessit/version"

        @apiSuccessExample {json} Success-Response:
            HTTP/1.1 200 OK
            {
              "version": "2.0"
            }
        """
        return {'version': guessit.__version__}

api.add_resource(GuessIt, '/guessit/')
api.add_resource(GuessItVersion, '/guessit/version/')


def main():  # pragma:no cover
    app.run(host='0.0.0.0')

if __name__ == '__main__':  # pragma:no cover
    main()
