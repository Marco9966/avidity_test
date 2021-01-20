from flask import Flask, render_template, request, redirect, session, flash, url_for
from assets import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', heroesTable = GetHeroesTable(10, 5))

app.run(debug=True)
