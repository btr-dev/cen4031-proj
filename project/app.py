from flask import Flask, request, render_template
import datetime
import time
import os

app = Flask(__name__)

class StopWatch:
    def __init__(self, startTime = 0, endTime = 0, elapsedTime = 0):
        self.__startTime = startTime
        self.__endTime = endTime
        self.__elapsedTime = elapsedTime

    def start(self):
        self.__startTime = time.clock()

    def stop(self):
        return self.getElapsedTime()

    def reset(self):
        self.__startTime = 0
        self.__elapsedTime = 0

    def getstarttime(self):
        return self.__startTime

    def getendtime(self):
        return self.__endTime

    def getElapsedTime(self):
        elapsedTime = self.__elapsedTime
        elapsedTime +=((time.clock() - self.__startTime) * 1000)
        return elapsedTime

@app.route("/", methods=["GET","POST"])
def elaspedTime():
    if request.method == "POST":
        elapsedTime = request.form.get("elapsedTime")
        ###double check if home.html is the correct destination
    return render_template("home.html",elapsedTime = elapsedTime)

if __name__ == '__main__':
    app.run(debug = True) 
