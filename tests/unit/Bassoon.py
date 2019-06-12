# -*- coding: utf-8 -*-
import os

from bassoon import Bassoon


def test_bassoon():
    assert Bassoon.defaults == {}


def test_bassoon_init(patch):
    patch.object(Bassoon, 'apply')
    Bassoon()
    assert Bassoon.apply.call_count == 1


def test_bassoon_apply(patch):
    patch.init(Bassoon)
    bassoon = Bassoon()
    bassoon.defaults = {'one': 'value'}
    bassoon.apply()
    assert bassoon.one == 'value'


def test_bassoon_apply_from_env(patch):
    patch.object(os, 'getenv', return_value='envvalue')
    patch.init(Bassoon)
    bassoon = Bassoon()
    bassoon.defaults = {'one': 'value'}
    bassoon.apply()
    assert bassoon.one == 'envvalue'


def test_bassoon_attribute_empty():
    assert Bassoon().option is None
