from dependency_injector import providers
from flask import Flask
from flask_cors import CORS
from .container import AppContainer
from blueprints import health_check, relay

def create_app() -> Flask:
  container = AppContainer()
  container.wire(modules=[health_check, relay])
  
  app = Flask(__name__)
  app.container = container
  CORS(app)
  
  app.register_blueprint(health_check.blueprint)
  app.register_blueprint(relay.blueprint)

  return app