#!/usr/bin/env python
# coding=utf-8
from __future__ import absolute_import, division, print_function

try:
    import v
except ImportError:
    import tools.v as v

def do_something():
    data = ""
    with open("resources/lol.txt") as f:
        data = f.read().strip()
    return "|keys|" + data + v.do_something()

print("K!")

if __name__ == "__main__":
    print("K main!")
    print(do_something())

