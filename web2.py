from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import csv

app = Flask(__name__, template_folder="templates")
GoogleMaps(app)

user_long = 121.060197
user_lat = 14.657576
bike_fleet = []

# make_bike creates a dictionary that represents a bike and its attributes
def make_bike(bike_ID,bike_status,bike_lat,bike_long):
    bike = {}
    bike['bike_ID'] = bike_ID
    bike['bike_status'] = bike_status
    bike['bike_lat'] = bike_lat
    bike['bike_long'] = bike_long

    return bike

def bike_distance(bike_number):
    distance = (user_lat - bike_fleet[bike_number]['bike_lat'])**2 + (user_long - bike_fleet[bike_number]['bike_long'])**2
    return distance

@app.route("/index")
def home ():
  return render_template("index.html")

@app.route("/login")
def login ():
    return render_template("LogIn.html")

@app.route("/signup")
def signup ():
    return render_template("SignUp.html")

@app.route("/timer")
def timer():
    return render_template("timer.html")

@app.route("/bikewaiting")
def bikewaiting():
    return render_template("waiting.html")

@app.route("/endtrip")
def endtrip():
    return render_template("end.html")

@app.route("/")
def mapview():
    markers = []
    bike_fleet = csv.reader(open("database_bikes.csv"))
    for bike in bike_fleet:
        if bike[1] == "locked":
            markers.append({
                'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
                'lat': bike[2],
                'lng': bike[3],
                'infobox': "<b>Hello World</b>"
            })
        else:
            pass
    sndmap = Map(
        identifier="sndmap",
        lat=14.655072,
        lng=121.068560,
        zoom=15,
        markers=markers
    )
    return render_template('map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)