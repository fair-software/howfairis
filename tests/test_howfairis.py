#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for the howfairis module.
"""
import pytest

from howfairis import howfairis


def test_something():
    assert True


def test_with_error():
    with pytest.raises(ValueError):
        # Do something that raises a ValueError
        raise(ValueError)


# Fixture example
@pytest.fixture
def an_object():
    return {}


def test_howfairis(an_object):
    assert an_object == {}
