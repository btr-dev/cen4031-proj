from flask import Flask, render_template, request
from stopWatch import StopWatch

app = Flask(__name__)
app.debug = True

# Create Timer object from stopwatch class 
timer = StopWatch(app)
# This would be the return point for the elapsed time data to be displayed to
# The website table.
headings = ("ID", "Duration")
data = timer.retrieveData()
previous = "0.0"

@app.route('/', methods=["GET", "POST"])
def index():
    global headings, data, previous
    if request.method == 'POST':
        if request.form['submit_button'] == 'START':
            timer.startTimer()
        elif request.form['submit_button'] == 'STOP':
            data = timer.stopTimer()
            #This number variable is our elapsed time that is displayed in the
            # text window.
            previous = str(data[-1][1])
    return render_template('home.html', TableHeadings=headings, TableData=data, Number=previous)

if __name__ =='__main__':
    app.run()
