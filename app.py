from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/quemsomos")
def quemSomos():
    return render_template("quemsomos.html")
