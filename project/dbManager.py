from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

# i think what i need is another class with the current functionality of dbmanager inside of it
# this is a mess, but i don't want the class definition to be in the stub

# a class that takes the database as an 
# no, because i can't define the class in the constructor
# i think it has to be done in the stub

class dbManager():

    def __init__(self, app):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'test.db')
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

    def add(self, time: float):
        new_time = self.WatchTime(duration = time)
        self.db.session.add(new_time)
        self.db.session.commit()

    def clear(self):
        self.WatchTime.query.delete()
        self.db.session.commit()