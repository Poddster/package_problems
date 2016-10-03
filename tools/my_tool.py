#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

try:
    import c, d, k, s
except ImportError:
    import tools.c as c
    import tools.d as d
    import tools.k as k
    import tools.s as s

print("my_tool!")
def do_something():
    return "|main tool!|" + d.do_something() + s.do_something() + k.do_something() + c.do_something()


if __name__ == "__main__":
    print("my_tool main!")
    print(do_something())
