#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2017 yu.liu <showmove@qq.com>
# All rights reserved


class model(dict):
    """简洁版MODEL
    => conf = model()
    => conf = [{'dd': {'cc': {'ee': {'xx' : 'test'}}}}, {'a': 'b'}]
    => print(conf.dd.cc.ee.xx)
    ```
    test
    ```
    """

    def __init__(self, *args, **kwarg):
        
        try:
            super().__init__(*args, **kwarg)
        except Exception as err:
            import ipdb
            ipdb.set_trace()

        for __attrbute in self.keys():
            setattr(self, __attrbute, self[__attrbute])

    def __values_to_model(self, value):

        if isinstance(value, (list, tuple, set)):
            _aval = []
            for _val in value:
                if isinstance(_val, dict):
                    _val = model(_val)
                elif isinstance(_val, (list, tuple, set)):
                    _val = self.__values_to_model(_val)
                _aval.append(_val)
            
            _aval = value.__class__(_aval)
            return _aval

        elif isinstance(value, dict):
            value = model(value)

        return value

    def __setattr__(self, key, value):
        
        try:
            
            if not hasattr(self, key):
                self[key] = value
                value = self.__values_to_model(value)
        except Exception as e:
            print(type(key), value)
            raise(e)
            

        super().__setattr__(key, value)

    def __getattr__(self, key):
        return super().__getattr__(self, key)

    def __getitem__(self, key):
        if hasattr(self, key):
            return getattr(self, key)
        elif key in self.keys():
            return self.get(key)
        else:
            return super().__getitem__(key)

    def __getattribute__(self, *args, **kwargs):

        return object.__getattribute__(self, *args, **kwargs)


class WithOperations(object):

    name = ''

    def __init__(self, name):
        self.name = name
        self.value = []

    def __setattr__(self, key, val):
        if key not in ['name', 'value']:
            try:
                self.value.append(" `{0}` = '{1}'".format(
                    key, "%(val)s" % {'val': val}))
            except Exception as e:
                raise(AttributeError)
        else:
            super().__setattr__(key, val)


class CursorReader(object):

    def __init__(self, name, primary_id='id'):
        self.name = name
        self.primary_id = primary_id

    def _or(self):
        pass


class CursorWriter(object):
    pass


if __name__ == "__main__":
    dicts = {'zz': {'weq': (1, {'a': 'b'}, ({'a': 'b'}, 2,2,2), 4)}, 'mysql': {'online': {'minFreeConnections': (11, 23, [2, 3, (1, 2, 3, {"1": 2}), 5]), 'maxConnections': 55, 'database': 'liuy', 'port': 3306, 'host': 'liuyu.info', 'user': 'liuy', 'password': 'a123456'}, 'dev': {'minFreeConnections': 11, 'maxConnections': 55, 'database': 'liuy', 'port': 3306, 'host': 'liuyu.info', 'user': 'liuy', 'password': 'a123456'}, 'test': {'minFreeConnections': 11, 'maxConnections': 55, 'database': 'liuy', 'port': 3306, 'host': 'liuyu.info', 'user': 'liuy', 'password': 'a123456'}}, 'logger': {
        'handlers': {'handler_http': {'url': '/logger/', 'level': 'INFO', 'host': '192.168.10.169:84', 'method': 'POST', 'formatter': 'format_def', 'class': 'logging.handlers.HTTPHandler'}}, 'version': 1, 'loggers': {'api': {'handlers': ['handler_http'], 'level': 'INFO', 'propagate': 0}, 'jobs': {'handlers': ['handler_http'], 'level': 'INFO', 'propagate': 0}}, 'formatters': {'format_def': {'format': '%(levelname)-8s %(asctime)s %(name)s %(ip)s %(method)s %(path)s %(message)s'}}}, 'redis': {}, 'mongo': {}}
    z = model(dicts)
    print(z.zz.weq[2][0])
