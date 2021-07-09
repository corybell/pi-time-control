import flask
from flask_cors import CORS
from dotenv import load_dotenv
from api.blueprints import register_blueprints

load_dotenv()

app = flask.Flask(__name__)

CORS(app)

register_blueprints(app)
