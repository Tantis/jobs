#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""定制错误代码

RESPONSE CODE:
    SUCCESS = 200
    FAILDS  = 400
"""
class Default(object):
    Success = 200
    Failed  = 400

class Login(Default):
    pass

class Register(Default):
    pass

class Information(Default):
    pass
