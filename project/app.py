from flask import Flask, request, render_template
import datetime
import time
import os

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
            return self.dbmgr.retrieve()
        return []
        
@app.route("/", methods=["GET","POST"])
def elaspedTime():
    if request.method == "POST":
        elapsedTime = request.form.get("elapsedTime")
        ###double check if home.html is the correct destination
    return render_template("home.html",elapsedTime = elapsedTime)

if __name__ == '__main__':
    app.run(debug = True) 
