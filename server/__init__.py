from flask import Flask
from flask import render_template
from flask import request
from flask_restplus import Api
from server.modules import model
from server.db import MySQLdb
import json


"""
I READLY GOOD GOGOGO

"""

app = Flask(__name__)

api = Api(app, version='1.0', title='Matchjobs API',
    description='2016-11-20 jobs Starting',
)

# 读取配置文件
with open('jobs_config.json', 'r', encoding='utf8') as __conf:
    conf = json.load(__conf)

configs = model(conf)
print(configs.mysql.dev)

db = MySQLdb(dict(configs.mysql.dev))


@app.route('/<string:url>')
def args(url):
    if not url:
        return render_template('index.html')
    return render_template(url)


@app.route('/index/<string:url>')
def index(url=None):

    return render_template('index.html')

    # return render_template('index.html')


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

from server import resource
