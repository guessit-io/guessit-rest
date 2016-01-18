REST WebService for GuessIt
===========================

.. image:: http://img.shields.io/pypi/v/guessit-rest.svg
    :target: https://pypi.python.org/pypi/guessit-rest
    :alt: Latest Version

.. image:: http://img.shields.io/badge/license-LGPLv3-blue.svg
    :target: https://pypi.python.org/pypi/guessit-rest
    :alt: LGPLv3 License

.. image:: http://img.shields.io/travis/guessit-io/guessit-rest.svg
    :target: https://travis-ci.org/guessit-io/guessit-rest
    :alt: Build Status

.. image:: http://img.shields.io/coveralls/guessit-io/guessit-rest.svg
    :target: https://coveralls.io/github/guessit-io/guessit-rest
    :alt: Coveralls

GuessIt is a python library that extracts as much information as possible from a video filename.

This is the REST WebService for `GuessIt <https://github.com/guessit-io/guessit>`_.

Install with pip
----------------

Python package is available on `PyPI <https://pypi.python.org/pypi/guessit-rest>`_.

    $ pip install guessit-rest

Then run guessit rest API using entry point.

    $ guessit-rest

Install from sources
--------------------

    $ git clone https://github.com/guessit-io/guessit-rest

    $ cd guessit-rest

Then configure a virtualenv with [pyenv](https://github.com/yyuu/pyenv) or any virtualenv manager you may like.

    $ pyenv virtualenv ...

Then install dependencies in the virtualenv.

    $ pip install -e .

Then run guessit rest API using main module.

    $ python -m guessitrest.app

Install with Docker
-------------------

An automated build is available at `Docker Hub <https://hub.docker.com/r/toilal/guessit-rest/>`_.

    $ docker run -p 5000:5000 -it toilal/guessit-rest

Usage
-----

Connect your browser to `http://localhost:5000/?filename=test.avi <http://localhost:5000/?filename=test.avi>`_

License
-------

GuessIt is licensed under the `LGPLv3 license <http://www.gnu.org/licenses/lgpl.html>`_.
