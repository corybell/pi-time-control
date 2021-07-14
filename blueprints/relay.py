from flask import Blueprint, jsonify, request
from dependency_injector.wiring import inject, Provide
from services.relay import RelayService
from app.container import AppContainer

blueprint = Blueprint('relay', __name__)

@blueprint.route('/relay/<string:id>/on', methods=['GET'])
@inject
def relay_get(id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  return jsonify({}), 200

@blueprint.route('/relay/<string:id>/off', methods=['GET'])
@inject
def relay_edit(id: str, relay_service: RelayService = Provide[AppContainer.relay_service]):
  return jsonify({}), 200