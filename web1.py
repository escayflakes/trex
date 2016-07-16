from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map

import csv

app = Flask(__name__, template_folder="templates")
GoogleMaps(app)

@app.route("/")
def mapview():
    sndmap = Map(
        identifier="sndmap",
        lat=14.655072,
        lng=121.068560,
        zoom=15,
        markers=[
          {
             'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
             'lat': 14.647323,
             'lng': 121.060197,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
             'lat': 14.657905,
             'lng': 121.060049,
             'infobox': "<b>Hello World from other place</b>"
          },
          {
             'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
             'lat': 14.657576,
             'lng': 121.074031,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
             'lat': 14.648329,
             'lng': 121.074190,
             'infobox': "<b>Hello World</b>"
          },
          {
             'icon': 'https://raw.githubusercontent.com/escayflakes/trex/master/tiny%20logo.png',
             'lat': 14.655072,
             'lng': 121.068560,
             'infobox': "<b>Hello World</b>"
          }
        ]
    )
    return render_template('map.html', sndmap=sndmap)

if __name__ == "__main__":
    app.run(debug=True)