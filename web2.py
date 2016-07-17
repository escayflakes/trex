from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import math
import csv

app = Flask(__name__, template_folder="templates")
GoogleMaps(app)

user_lng = 121.074190
user_lat = 14.648329
bike_fleet = []

def bike_distance(bike_number):
    distance = math.sqrt((user_lat - bike_fleet[bike_number][2])**2 + (user_lng - bike_fleet[bike_number][3])**2)
    return distance

# page linking
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
    nearest_bike = []
    shortest_distance = 99999999
    current_distance = 0
    bike_fleet = csv.reader(open("database_bikes.csv"))
    for bike in bike_fleet:
        if bike[1] == "locked":
            current_distance = math.sqrt((user_lat - float(bike[2]))**2 + (user_lng - float(bike[3]))**2)
            if current_distance < shortest_distance:
                shortest_distance = current_distance
                nearest_bike = bike
            else:
                pass
        else:
            pass
    wait_map = Map(
        identifier="wait_map",
        lat=nearest_bike[2],
        lng=nearest_bike[3],
        zoom=15,
        markers=[
        {
        'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
        'lat': nearest_bike[2],
        'lng': nearest_bike[3],
        'infobox': "<b>Unlock me now!</b>"
        },
        {
         'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
         'lat': user_lat,
         'lng': user_lng,
         'infobox': "<b>You are here</b>"
        }]
    )
    return render_template("waiting.html",wait_map=wait_map)

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
                'infobox': "<b>Open to reservation</b>"
            })
        else:
            pass
    markers.append({
         'icon': 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png',
         'lat': user_lat,
         'lng': user_lng,
         'infobox': "<b>You are here</b>"
        })
    sndmap = Map(
        identifier="sndmap",
        lat=user_lat,
        lng=user_lng,
        zoom=16,
        markers=markers
    )
    return render_template('map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)