from flask import Flask, render_template, render_template_string
from flask import jsonify
from flask_cors import CORS, cross_origin
import win32print
import os

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
def home():
   return render_template('home.html')

@app.route("/track/<id>")
def get_parcel(id):
   #take the id parameter and query the db with it
   return jsonify(
        idn = id,
        nameOfDriver = "John",
        status = "In transit",
        eta = "23 minutes",
        dispatchTime = "2pm",
        address = "33 Pain Street, london S4 7GP"
    )

@app.route("/directions/<id>")
def get_directions(id):
    return jsonify(
        idn = id,
        latitude = "",
        longitude = "",
        accuracy = ""
    )

if __name__ == '__main__':
   app.run(debug=True)
