from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import csv

app = Flask(__name__, template_folder="templates")
GoogleMaps(app)

# a list of dictionaries representing bikes generated from make_bike()
bike_fleet = []

# make_bike creates a dictionary that represents a bike and its attributes
def make_bike(bike_ID,bike_status,bike_lat,bike_long):
    bike = {}
    bike['bike_ID'] = bike_ID
    bike['bike_status'] = bike_status
    bike['bike_lat'] = bike_lat
    bike['bike_long'] = bike_long

    return bike

# function that adds a bike(dictionary) to the list, bike_fleet
def populate_tracker():
    bike_fleet.append(make_bike(1,"unlocked",14.6473235,121.060197))
    bike_fleet.append(make_bike(2,"broken",14.657905,121.060049))
    bike_fleet.append(make_bike(3,"locked",14.657576,121.074031))
    bike_fleet.append(make_bike(4,"unlocked",14.648329,121.074190))

@app.route("/Home")
def home ():
  return render_template("index.html")

@app.route("/")
def mapview():
    populate_tracker()
    sndmap = Map(
        identifier="sndmap",
        lat=14.655072,
        lng=121.068560,
        zoom=15,
        markers=[
              {
                 'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
                 'lat': bike_fleet[0]['bike_lat'],
                 'lng': bike_fleet[0]['bike_long'],
                 'infobox': "<b>Hello World</b>"
              },
              {
                 'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
                 'lat': bike_fleet[1]['bike_lat'],
                 'lng': bike_fleet[1]['bike_long'],
                 'infobox': "<b>Hello World</b>"
              },
              {
                 'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
                 'lat': bike_fleet[2]['bike_lat'],
                 'lng': bike_fleet[2]['bike_long'],
                 'infobox': "<b>Hello World</b>"
              },
              {
                 'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
                 'lat': bike_fleet[3]['bike_lat'],
                 'lng': bike_fleet[3]['bike_long'],
                 'infobox': "<b>Hello World</b>"
              }
        ]
    )
    return render_template('map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)