# -*- coding: utf-8 -*-
from pytest import fixture


@fixture
def patch_init(mocker):
    """
    Makes patching a class' constructor slightly easier
    """
    def patch_init(item):
        mocker.patch.object(item, '__init__', return_value=None)
    return patch_init


@fixture
def patch(mocker, patch_init):
    mocker.patch.init = patch_init
    return mocker.patch
