from flask import current_app
from neo4j import time
import datetime

class MovieDao:
    
    def getAllMovies(self):
        with current_app.driver.session() as session:
            query = """
                    match (m:Movie) return m
                """
            moviesList = session.run(query)
            output = [self.node_to_dict(row['m']) for row in moviesList]
        return output
    
    def node_to_dict(self, node):
        node_dict = dict(node)
        for key, value in node_dict.items():
            if isinstance(value, (datetime.date, datetime.datetime, time.Date)):
                node_dict[key] = value.isoformat()  # Convert Date/Datetime to string in ISO format (YYYY-MM-DD)
        return node_dict