from flask import Blueprint, jsonify

health_check_controller = Blueprint('health_check_controller', __name__)

@health_check_controller.route('/health-check', methods=['GET'])
def health_check():
  return jsonify(version='1.0.0'), 200
