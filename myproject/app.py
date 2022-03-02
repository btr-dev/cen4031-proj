from flask import Flask, render_template, request
from data import Articles
import stop_watch

app = Flask(__name__)
app.debug = True

Articles = Articles()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/articles')
def articles():
    return render_template('articles.html',articles = Articles)

@app.route('/article/<string:id>/')
def article(id):
    return render_template('article.html',id=id)

@app.route('/', methods=["GET", "POST"])
def button():
    if request.method == 'POST':
        if request.form['submit_button'] == 'START':
            stop_watch.startTimer()
            return render_template('home.html')
        elif request.form['submit_button'] == 'STOP':
            print("test2")
            return render_template('articles.html')
    elif request.method == 'GET':
        print("test4")
        return render_template('about.html')

if __name__ =='__main__':
    app.run()
