#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

import tools.c as c

def test_c():
    assert c.do_something() == "|config|"
