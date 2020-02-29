from sanic import Blueprint
from sanic_api.handlers.nlp_handler import Analysis

nlp_blueprint = Blueprint(name='nlp', url_prefix='/nlp/api/v1')
nlp_blueprint.add_route(Analysis.as_view(), "/analysis")
