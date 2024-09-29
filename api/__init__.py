import datetime
import os
from api.routes.movies import movie_routes
from flask import current_app, jsonify, Flask
from dao.db_connection import init_driver
from neo4j import time

app = Flask(__name__)

app.config.from_mapping(
        NEO4J_URI=os.getenv('NEO4J_URI'),
        NEO4J_USERNAME=os.getenv('NEO4J_USERNAME'),
        NEO4J_PASSWORD=os.getenv('NEO4J_PASSWORD'),
        NEO4J_DATABASE=os.getenv('NEO4J_DATABASE'),
)


with app.app_context():
        driver = init_driver(
            app.config.get('NEO4J_URI'),
            app.config.get('NEO4J_USERNAME'),
            app.config.get('NEO4J_PASSWORD'),
            app.config.get('NEO4J_DATABASE')
        )

app.register_blueprint(movie_routes)