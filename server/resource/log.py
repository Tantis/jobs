#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2017 yu.liu <showmove@qq.com>
# All rights reserved

"""
远端日志服务

"""
import time

from flask import request
from flask_restplus import Api, Resource

from server.modules.utils import Request as Crawler
from server.operation.register import Register
from server import db
from .. import api


class LoggerServer(Resource):
    """日志服务器
    :POST : 存储日志信息
    :GET  : 获取日志信息
    """

    def post(self):
        """存储日志信息

        """
        try:
            level = request.form['levelname']
            msg = request.form['msg']
            funcname = request.form['funcName']
            funcmode = request.form['module']
            funcproc = request.form['process']
            filepath = request.form['pathname']
            logsname = request.form['name']

            db.insert(
                """INSERT INTO  `logger`
                                (
                                `level`,
                                `modules`,
                                `name`,
                                `filepath`,
                                `content`,
                                `other`,
                                `create_time`
                                )
                    VALUES (
                            :level,
                            :modules,
                            :name,
                            :filepath,
                            :content,
                            :other,
                            :create_time);
                """, {
                    "content": msg,
                    "level": level,
                    "modules": funcmode,
                    "name": logsname,
                    "filepath": filepath,
                    "other": "func: %s, proc: %s" % (funcname, funcproc),
                    "create_time": int(time.time())
                }
            )
            return {
                "status": 200,
                "msg": "成功"
            }
        except Exception as err:
            print(err)
            return {"status": 400, "msg": "失败"}, 400

# 创建
ns = api.namespace('logger', 
                    description="日志服务")

ns.add_resource(LoggerServer, '/')
