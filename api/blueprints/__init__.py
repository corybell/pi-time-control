from api.blueprints.health_check import health_check_controller

def register_blueprints(app):
  app.register_blueprint(health_check_controller)