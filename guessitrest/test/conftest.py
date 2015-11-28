#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from ..app import app as app_


@pytest.fixture
def app():
    return app_
