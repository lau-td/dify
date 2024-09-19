from flask import Blueprint
from libs.external_api import ExternalApi

bp = Blueprint("codelight_api", __name__, url_prefix="/v1/codelight")
api = ExternalApi(bp)


from .console_api import dataset
from .internal_api import (account, app, auth, model_config, model_providers,
                           tenant)
