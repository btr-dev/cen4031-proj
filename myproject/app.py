from flask import Flask, render_template, request
import flask_table
import dbManager
from data import Articles
import stop_watch
import jinja2

app = Flask(__name__)
app.debug = True

Articles = Articles()

# Create Timer object from stopwatch class 
timer = stop_watch.StopWatch(app)
# This would be the return point for the elapsed time data to be displayed to
# The website table.
headings = ("Time", "Word")
data = ( ("Test", "Hello"),
    ("Test2", "Hello"),
    ("Test3", "Hello"),
    ("Test4", "Hello")
)

@app.route('/')
def index():
    return render_template('home.html', Number="00:00:00")

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

@app.route("/")
def table():
    return render_template("home.html", headings=headings, data=data)

@app.route('/', methods=["GET", "POST"])
def button():
    return render_template("home.html", headings=headings, data=data)
    if request.method == 'POST':
        if request.form['submit_button'] == 'START':
            timer.startTimer()
            return render_template('home.html')
        elif request.form['submit_button'] == 'STOP':
            timer.stopTimer()
            #This number variable is our elapsed time that is displayed in the
            # text window.
            return render_template('home.html', Number=timer.getElapsedTime())
    elif request.method == 'GET':
        print("test4")
        return render_template('about.html')

if __name__ =='__main__':
    app.run()
