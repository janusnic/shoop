# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals
from shoop.notify.conditions.simple import IntegerEqual, NonEmpty, TextEqual, Empty
from shoop.notify.script import Context


def test_integer_equals():
    ie = IntegerEqual({"v1": {"variable": "v"}, "v2": {"constant": 42}})
    assert ie.test(Context.from_variables(v=42))
    assert ie.test(Context.from_variables(v="42"))
    assert not ie.test(Context.from_variables(v="442"))
    assert not ie.test(Context.from_variables(v=True))


def test_text_equal():
    ie = TextEqual({"v1": {"variable": "v"}, "v2": {"constant": "   Foo   "}})
    assert ie.test(Context.from_variables(v="foo"))
    assert ie.test(Context.from_variables(v="Foo"))
    assert ie.test(Context.from_variables(v="Foo  "))
    assert not ie.test(Context.from_variables(v="faa"))


def test_non_empty():
    ie = NonEmpty({"v": {"variable": "v"}})
    assert ie.test(Context.from_variables(v=True))
    assert not ie.test(Context.from_variables(v=""))
    assert not ie.test(Context.from_variables(v=0))


def test_empty():
    ie = Empty({"v": {"variable": "v"}})
    assert ie.test(Context.from_variables(v=False))
    assert ie.test(Context.from_variables(v=()))
    assert ie.test(Context.from_variables(v=0))
    assert not ie.test(Context.from_variables(v=6))
