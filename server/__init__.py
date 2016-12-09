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




from server import resource
from server import index
