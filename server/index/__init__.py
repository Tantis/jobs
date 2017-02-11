#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Copyright (c) 2016 yu.liu <showmove@qq.com>
# All rights reserved

"""网页驱动模块

"""
from server import app
from flask import render_template
from flask import request
from flask import Markup
from flask import jsonify
from server import db
from datetime import datetime
import os
import requests
import time
import random


@app.route('/constam/')
def home():
    """
    个人主页
    """
    return render_template('/home/index.html')

@app.route('/upload/')
def upload():
    """
    文件上传
    """
    return render_template('/utils/upload.html')

@app.route('/api/upload/', methods=['GET', 'POST'])
def uploads():
    """
    文件上传
    """
    current_time = int(time.time())
    try:
        if request.method == 'POST':
            f = request.files
            for item in f.listvalues():
                for value in item:
                    names = value.filename.split('.')[-1]
                    save_file_names = str(int(time.time())) + "_" + str(random.randint(0, 100000)) +'.'+ names
                    db.insert("""
                    INSERT INTO `work_image`
                                (
                                `url`,
                                `name`,
                                `create_time`)
                    VALUES (
                            :url,
                            :name,
                            :create_time);
                    """, {'create_time': current_time, 'name': value.filename.split('.')[0], 'url': '/static/img/%s' % save_file_names})
                    value.save('server/static/img/%s' % (save_file_names))
            return jsonify({'status': 200, 'data': save_file_names, 'msg': '成功'}), 200
        else:
            return jsonify({'status': 400, 'data': save_file_names, 'msg': '失败'}), 400
    except Exception as err:
        print(err)
        return jsonify({'status': 400, 'data': save_file_names, 'msg': '失败'}), 400

@app.route('/')
@app.route('/index/')
def constam():
    """
    关系图
    """

    ip = request.remote_addr
    headers = request.headers
    # 记录访问日志
    with open('access.log', 'a') as f:
        f.write('header: %s, datetime: %s, ip: %s \n' % (repr(headers), str(datetime.now()), ip))

    header_one = r"/static/img/timg.jpg"
    top_image = r"/static/img/awsd.png"
    top_title = Markup(r"岁月不饶人，<br \> 我亦未曾饶过岁月。")
    top_content = Markup(r"只有作出了正确的选择，人生的画卷才会更加美丽，人生的舞剧才会更加精彩。")
    top_link = Markup(
        r'<a class="caption-link" href="constam#" role="button"></a>')
    project_data = db.query("SELECT * FROM `work_projects` WHERE is_hide=0")
    for k, v in enumerate(project_data):
        v['project_content'] = Markup(v['project_content'])
        project_data[k] = v
    work_data = db.query(
        "SELECT * FROM `work_experience` WHERE is_hide=0 ORDER BY sort DESC ")
    for k, v in enumerate(work_data):
        v['work_content'] = Markup(v['work_content'])
        work_data[k] = v

    friends_data = db.query("SELECT * FROM work_firends WHERE is_hide=0 ")
    for k, v in enumerate(friends_data):
        v['content'] = Markup(v['content'])
        friends_data[k] = v

    skill_left_data = db.query("""
    SELECT * FROM `work_skill` WHERE is_hide=0 AND dis_code=1
    """)
    skill_right_data = db.query("""
    SELECT * FROM `work_skill` WHERE is_hide=0 AND dis_code=2
    """)

    case_data = db.query("SELECT * FROM `work_case` WHERE is_hide=0")
    for k, v in enumerate(case_data):
        v['content'] = Markup(v['content'])
        case_data[k] = v

    work_link = db.query("SELECT * FROM `work_links` WHERE is_hide=0")

    return render_template('/body/constam.html', title="liuyu的个人简历",
                           top_image=top_image,
                           top_title=top_title,
                           top_content=top_content,
                           top_link=top_link,
                           header_one=header_one,
                           project_data=project_data,
                           work_data=work_data,
                           friends_data=friends_data,
                           skill_left_data=skill_left_data,
                           skill_right_data=skill_right_data,
                           case_data=case_data,
                           work_link=work_link
                           )


@app.route('/profile/<int:id>')
def profile(id=1):
    
    return render_template('/home/profile.html')

@app.route('/access/')
def access():
    import json
    import os
    addr = {}
    if os.path.exists('addr.log'):
        with open('addr.log', 'r') as f:
            addr = json.load(f)
    return render_template('/body/access.html', addr=addr)


    
