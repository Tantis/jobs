#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2015 yu.liu <showmove@qq.com>
# All rights reserved

from functools import wraps

class Event(object):

    @staticmethod
    def get(response):
        print(response)
        #import ipdb; ipdb.set_trace()
        return response

def details(func):

    @wraps(func)
    def __console():
        print(func())
        x, y = func()
        if x:
            return Event.get(y)
        return Event.get(y)
    return __console

def wapper(func):
    def __console(*args, **kwargs):
        ok, response = func()
        return Event.get(response)
    return __console


@wapper
def test():
    return True, {'a': 'b', 'b': 'c'}

if __name__ == "__main__":

    p = test()
