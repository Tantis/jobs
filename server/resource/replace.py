from flask_restplus import Resource, Api
from .. import api
from server.operation.register import Register
from server import db
from flask import request

ns = api.namespace('opeartion', description="用户留言")


class Opeartion(Resource):
    """
    用户留言模块


    """

    def get(self):
        """
        查看用户留言

        """
        return {'status': 200, 'msg': '暂不开放'}

    def post(self):
        "用户留言模块"
        try:
            kwords = request.json
        except Exception as err:

            return {'status': 400, 'msg': '失败，你的数据格式不对 %s' % err}
        if not kwords:
            return {'status': 400, 'msg': '失败，你的数据格式不对'}
        kwargs = {}
        try:
            kwargs['msg'] = kwords['msg']
            kwargs['mobile'] = kwords['mobile']
            kwargs['name'] = kwords['name']
        except Exception as e:
            return {'status': 400, 'msg': '失败，你的数据格式不对 %s ' % e}
        result = db.insert("""
        insert into 
        work_msg (mobile, name, content)
        value (:mobile, :name, :msg)
        """, kwargs)
        if result:
            return {'status': 200, 'msg': '成功'}
        return {'status': 400, 'msg': '失败，你的数据格式不对'}

ns.add_resource(Opeartion, '/')
