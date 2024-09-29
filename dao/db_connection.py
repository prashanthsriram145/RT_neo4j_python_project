from flask import Flask, current_app
from neo4j import GraphDatabase

def init_driver(db_uri, username, password, database):
    with GraphDatabase.driver(db_uri, auth=(username, password), database=database) as driver:
        current_app.driver = driver
        driver.verify_connectivity()
    return current_app.driver

def get_driver():
    return current_app.driver

def close_driver():
    if current_app.driver != None:
        current_app.driver.close()
        current_app.driver = None

        return current_app.driver
