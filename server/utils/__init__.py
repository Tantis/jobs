#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""装饰模块


"""


def wapper(func):
    ok, response = func()
    def __console(tofunc, *args, **kwrag):
        return fucn(args, kwarg)
    return __console
