from flask import Flask
import time
from dbManager import dbManager

app = Flask(__name__)

class StopWatch:
    def __init__(self, flask_app):
        self.start_time = 0
        self.stop_time = 0 
        self.running = False
        self.dbmgr = dbManager(flask_app)

    def startTimer(self):
        if self.running == False:
           self.start_time = time.time() 
           self.running = True
        return self.start_time
    
    def stopTimer(self):
        if self.running == True:
            self.stop_time = time.time()
            self.dbmgr.add(self.stop_time - self.start_time)
            self.running = False
            return self.retrieveData()
        return []

    def retrieveData(self):
        return self.dbmgr.retrieve()
