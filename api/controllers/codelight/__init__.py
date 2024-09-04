from flask import Blueprint

from libs.external_api import ExternalApi

bp = Blueprint("codelight_api", __name__, url_prefix="/v1/codelight")
api = ExternalApi(bp)


from .internal_api import account, tenant, model_providers, app, model_config, auth
