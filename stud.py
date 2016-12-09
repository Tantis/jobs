#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2015 yu.liu <showmove@qq.com>
# All rights reserved

from functools import wraps

class Event(object):

    @staticmethod
    def get(response):
        print(response)
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

def wapper(f):
    """参数效验


    """
    def __install(**params):
        avatar = {}
        for _par in params:
            avatar[_par] = params[_par]
        
        def __decotors(func):
            @wraps(func)
            def __console(*args, **kwargs):
                
                ok, response = func(**kwargs)
                for item in response:
                    if item in avatar.keys():
                        if not isinstance(response[item], avatar[item]):
                            return f(False, {'status': 100403, 'msg': '参数传递错误'}), 403
                        continue
                return f(True, response)

            return __console
        return __decotors
    return __install

@wapper
def test():
    return True, {'a': 'b', 'b': 'c'}

if __name__ == "__main__":

    @wapper
    def orages(ok, response):
        return ok, response
   
    @orages(k=int, g=int)
    def wappers():
        return True, {'k': 'b', 'g': 'c'}
    
    x = wappers()
    print(x)