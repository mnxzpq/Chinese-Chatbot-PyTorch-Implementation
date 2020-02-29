from sanic.views import HTTPMethodView
from sanic.response import json as jsp
from asgiref.sync import sync_to_async
from sanic_api.models.api import robot
import json


class Analysis(HTTPMethodView):
    async def post(self, request):
        data = json.loads(request.json)
        req_text = data.get("req_text")
        rsp_text = await sync_to_async(robot.answer)(req_text)
        rsp_status = 200
        if rsp_text == "</UNK>":
            rsp_status = 404
        return jsp({"rsp_text": rsp_text}, status=rsp_status)
