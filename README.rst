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

Run with Docker
---------------

An automated build is available at `Docker Hub <https://hub.docker.com/r/toilal/guessit-rest/>`_.

    $ docker run -p 5000:5000 -it toilal/guessit-rest

Run from sources
----------------

    $ python guessitrest

Usage
-----

Connect your browser to `http://localhost:5000/?filename=test.avi <http://localhost:5000/?filename=test.avi>`_

Some options are available through command line arguments.

```
usage: guessitrest [-h] [-l LISTENING_ADRESS] [-p LISTENING_PORT]

optional arguments:
  -h, --help            show this help message and exit
  -l LISTENING_ADRESS, --listening-adress LISTENING_ADRESS
                        Listening IP Adress of the HTTP Server.
  -p LISTENING_PORT, --listening-port LISTENING_PORT
                        Listening TCP Port of the HTTP Server.
```

License
-------

GuessIt is licensed under the `LGPLv3 license <http://www.gnu.org/licenses/lgpl.html>`_.
