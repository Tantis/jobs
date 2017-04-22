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