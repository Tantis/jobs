#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""网页驱动模块

"""
from server import app


@app.route('/<string:url>')
def args(url):
    if not url:
        return render_template('index.html')
    return render_template(url)

@app.route('/index/<string:url>')
def index(url=None):

    return render_template('index.html')


@app.route('/diagram')
def details():
    return render_template('diagram.html')


@app.route('/output')
def output():
    return render_template('output.html')


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/button')
def button():
    return render_template('button.html')
