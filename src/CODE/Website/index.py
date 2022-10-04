from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")

@app.route('/designer/')
def designer():
    return render_template("designer.html")

@app.route('/stats/')
def stats():
    return render_template("stats.html")

