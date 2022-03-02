from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

# dbManager class
# Class meant to be used by application layer as a means of adding
# to and retrieving from the database

class dbManager():

    # Takes a Flask object as argument
    # Connects the provided Flask object to the database
    # and defines a WatchTime table with an automatically incrementing
    # integer as the primary key, and a float holding the duration of a stopwatch run
    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')
        self.db = SQLAlchemy(app)


        class WatchTime(self.db.Model):
            id = self.db.Column(self.db.Integer, primary_key = True)
            duration = self.db.Column(self.db.Float, unique = False, nullable = False)

        self.WatchTime = WatchTime

        self.db.create_all()

    # Queries database and returns data stored in the WatchTime table
    # in the form of a list of tuples.
    def retrieve(self):
        time_data = self.WatchTime.query.all()
        result = []
        for d in range(time_data.__len__()):
            result.append((time_data[d].__dict__['id'], time_data[d].__dict__['duration']))
        return result

    # Takes a float as argument
    # Adds a new entry to the database with an autoincrementing ID and
    # the provided float as duration
    def add(self, time: float):
        new_time = self.WatchTime(duration = time)
        self.db.session.add(new_time)
        self.db.session.commit()
