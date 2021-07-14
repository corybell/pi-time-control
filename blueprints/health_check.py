from flask import Blueprint, jsonify
from dependency_injector.providers import Configuration
from dependency_injector.wiring import inject, Provide
from app.container import AppContainer
from app.version import version

blueprint = Blueprint('health_check', __name__)

@blueprint.route('/health-check', methods=['GET'])
@inject
def health_check(config: Configuration = Provide[AppContainer.config]):
  return jsonify(version=version, config=config), 200
