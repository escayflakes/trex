from flask import Flask
from flask import render_template

import csv

y = 12
x = 5
app = Flask(__name__)

@app.route("/") #home function 
def main(): #runs as html
	pokemon = csv.reader(open("pokemon.csv"))
	return render_template("index.html",x=12*y, pokemon = pokemon)

@app.route("/youthhack")
def youthhack():
	return render_template("index.html",x=99)

@app.route("/<username>")
def apples(username):
	return render_template("index.html",x=username)



app.debug = True
app.run()
