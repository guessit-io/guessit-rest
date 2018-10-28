#!/usr/bin/env python
# -*- coding: utf-8 -*-

from guessitrest.app import app
from guessitrest.bootstrap import bootstrap


def main():
    bootstrap(app)


if __name__ == '__main__':  # pragma:no cover
    main()
