import datetime
from dao import movies
from flask import Blueprint, jsonify
from neo4j import time

movie_routes = Blueprint("movies", __name__, url_prefix="/api/movies")

@movie_routes.get("/getMovies")
def getMovies():
    movieDao = movies.MovieDao()
    output = movieDao.getAllMovies()
    return jsonify(output)

