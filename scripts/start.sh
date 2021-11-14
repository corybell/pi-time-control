#!/bin/bash

export FLASK_APP=./app
flask run --host=$API_HOST --port=$API_PORT --cert=adhoc