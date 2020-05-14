from flask import Flask, render_template, request, redirect, url_for
import os
app = Flask(__name__)

@app.after_request
def add_header(r):
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    return r

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return "About page under construction"

@app.route('/markets')
def markets():
    return "Jerome Powell's printer is warm today."

@app.route('/login')
def login():
    return "Login page under construction."

if __name__ == '__main__':
    app.run(debug=True)
