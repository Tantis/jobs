from flask_restplus import fields
from server.response.code import build_result
from server.response.code import DefaultStatus
from server import api

response_list_data = api.model("返回数据", {})

response_code_200_modules = api.response(200, "成功",
    model=api.model(
        "response_success", {"status": fields.Integer(200, description="状态CODE"),
                             "msg": fields.String(DefaultStatus.Decriptions[200])
        }
    )
)

response_code_404_modules = api.response(404, "成功",
    model=api.model(
        "response_success", {"status": fields.Integer(404, description="状态CODE"),
                             "msg": fields.String(DefaultStatus.Decriptions[404])
        }
    )
)




class DocumentFormart:
    
    __swich_fields_keys = {
        "str": fields.String,
        "int": fields.Integer,
        "float": fields.Float,
        "Decimal":fields.Arbitrary,
    }

    @classmethod
    def NestedList(self, data):
        """返回列表中的数据

        """
        _fileds = {}
        for _key in data:
            if isinstance(_key, dict):
                _fileds = self.NestedDict(_key)
        return _fileds

    @classmethod
    def NestedDict(self, data):
        """返回字典里面的数据

        """
        return self.ResponseBody(data, "", response_fileds=True)

    @classmethod
    def ResponseBody(self, data, model_name, response_model="model", response_code="200", response_data="成功", response_templates=None, response_fileds=False):
        """返回整个BODY
        :params data          : response data
        :params response_model: model | response
        :return : response data model
        """

        models = {}
        for _key in data:
            if isinstance(data[_key], dict):
                _fields =  fields.Nested(model=api.model(_key, self.NestedList(data[_key])))
            elif isinstance(data[_key], list):
                _fields =  fields.List(fields.Nested(model=api.model(_key, self.NestedList(data[_key]))))
            else:
                _fields = self.__swich_fields_keys[data[_key].__class__.__name__](data[_key], Description=data[_key])
            models[_key] = _fields
        if response_fileds:
            return models
        if response_model == "response":
            return api.response(
                response_code, response_data, model=api.model(model_name, models))
            
        return api.doc(body=api.model(model_name, models))