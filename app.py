from flask import Flask, render_template, render_template_string
from flask import jsonify
from flask_cors import CORS, cross_origin

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

@app.get("/directions/<id>")
def get_directions(id):
    
    #GET THE DIRECTION DATA FROM DATABASE
    #FOR THE EXAMPLE I WILL JUST USE DUMMY DATA
    directions = [{"field1": "field1 data"},
                  {"field1": "field2 data"}]
    
    """
        Any data you want to pass to the template you just
        list it as a keyword argument 
        e.g if you wanted to add a variable for user
        you would just add user=user_object 
    """
    return  render_template("directions.html", 
                            directions=directions)

if __name__ == '__main__':
   app.run(debug=True)
