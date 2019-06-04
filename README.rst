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

.. code:: shell

    $ pip install guessit-rest

Then run guessit rest API using entry point.

.. code:: shell

    $ guessit-rest

Install from sources
--------------------
.. code:: shell

    $ git clone https://github.com/guessit-io/guessit-rest
    $ cd guessit-rest

Then configure a virtualenv with `pyenv <https://github.com/yyuu/pyenv>`_ or any virtualenv manager you may like.

.. code:: shell

    $ pyenv virtualenv ...

Then install dependencies in the virtualenv.

.. code:: shell

    $ pip install -e .

Then run guessit rest API using main module.

.. code:: shell

    $ python guessitrest

Run with Docker
---------------

An automated build is available at `Docker Hub <https://hub.docker.com/r/guessit/guessit-rest/>`_.

.. code:: shell

    $ docker run -p 5000:80 -it guessit/guessit-rest

Usage
-----

Connect your browser to `http://localhost:5000/?filename=test.avi <http://localhost:5000/?filename=test.avi>`_

API Documentation is available on
`Swagger UI <http://petstore.swagger.io/?url=https://raw.githubusercontent.com/guessit-io/guessit-rest/master/swagger.yaml>`_

A test server is available on `https://api.guessit.io <https://api.guessit.io>`_. This server has a small API rate limit,
so if you really need a GuessIt REST API, you have to host it on your own server.

.. code::

    usage: guessitrest [-h] [-l LISTENING_ADRESS] [-p LISTENING_PORT]

    optional arguments:
      -h, --help            show this help message and exit
      -l LISTENING_ADRESS, --listening-adress LISTENING_ADRESS
                            Listening IP Adress of the HTTP Server.
      -p LISTENING_PORT, --listening-port LISTENING_PORT
                            Listening TCP Port of the HTTP Server.

flask-restful
-------------

This project currently use a `fork of flask-restful <https://github.com/Toilal/flask-restful>`_. See
`flask-restful/flask-restful#645 <https://github.com/flask-restful/flask-restful/pull/645>`_.

As a workaround, we use a copy of the forked flask-restul module to make it available from sources.

You can still run REST API with original flask-restful, but using POST with multiple filenames on ```/list/```
resource is broken.

License
-------

GuessIt is licensed under the `LGPLv3 license <http://www.gnu.org/licenses/lgpl.html>`_.
